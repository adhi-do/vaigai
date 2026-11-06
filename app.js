/**
 * VAIGAI'S IKIGAI — Interactive Newspaper & Book Publication
 * High-End Heyzine-Inspired Viewer Engine
 * Includes Proportional Aspect Ratio, Web Audio Synthesis, Responsive Sizing & Dual Modes
 */

document.addEventListener('DOMContentLoaded', () => {
  // --- DOM Elements ---
  const brandLink = document.getElementById('brand-link');
  
  const flipbookContainer = document.getElementById('flipbook-container');
  const flipbookElement = document.getElementById('flipbook');
  const flipbookViewport = document.getElementById('flipbook-viewport');
  const gazetteContainer = document.getElementById('gazette-container');
  
  const btnPrev = document.getElementById('btn-prev-page');
  const btnNext = document.getElementById('btn-next-page');
  const btnDockPrev = document.getElementById('btn-dock-prev');
  const btnDockNext = document.getElementById('btn-dock-next');
  
  const pageIndicator = document.getElementById('page-indicator');
  const pageScrubber = document.getElementById('page-scrubber');
  
  const btnModeToggle = document.getElementById('btn-mode-toggle');
  const modeLabel = document.getElementById('mode-label');
  
  const btnToc = document.getElementById('btn-toc');
  const btnDockToc = document.getElementById('btn-dock-toc');
  const btnTocClose = document.getElementById('btn-toc-close');
  const tocDrawer = document.getElementById('toc-drawer');
  const modalBackdrop = document.getElementById('modal-backdrop');
  
  const btnToggleThumbs = document.getElementById('btn-toggle-thumbs');
  const thumbnailStrip = document.getElementById('thumbnail-strip') || document.getElementById('thumb-bar-drawer');
  
  const btnAudio = document.getElementById('btn-audio');
  const audioIcon = document.getElementById('audio-icon');
  
  const themeSelect = document.getElementById('theme-select');
  const btnFullscreen = document.getElementById('btn-fullscreen');
  const btnPrint = document.getElementById('btn-print');
  
  const originalFlipbookHTML = flipbookElement ? flipbookElement.innerHTML : '';
  
  const btnZoomIn = document.getElementById('btn-zoom-in');
  const btnZoomOut = document.getElementById('btn-zoom-out');
  const btnZoomReset = document.getElementById('btn-zoom-reset');
  const zoomLevelDisplay = document.getElementById('zoom-level');
  
  const lightboxModal = document.getElementById('lightbox-modal');
  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxImgFrame = document.getElementById('lightbox-img-frame');
  const lightboxCaption = document.getElementById('lightbox-caption');
  const lightboxCaptionHint = document.getElementById('lightbox-caption-hint');
  const lightboxClose = document.getElementById('lightbox-close');
  const lightboxToggleInfo = document.getElementById('lightbox-toggle-info');
  const lightboxInfoBtnLabel = document.getElementById('lightbox-info-btn-label');
  const lightboxJumpPage = document.getElementById('lightbox-jump-page');
  const lightboxEventTag = document.getElementById('lightbox-tag-text');
  const lightboxInfoDept = document.getElementById('lightbox-info-dept');
  const lightboxInfoDate = document.getElementById('lightbox-info-date');
  const lightboxInfoTitle = document.getElementById('lightbox-info-title');
  const lightboxInfoByline = document.getElementById('lightbox-info-byline');
  const lightboxInfoBody = document.getElementById('lightbox-info-body');
  const lightboxContentContainer = document.getElementById('lightbox-content-container');
  
  const gazetteSearchInput = document.getElementById('gazette-search-input');
  
  // --- State Variables ---
  let pageFlip = null;
  let currentPage = 1;
  const totalPages = (flipbookElement ? flipbookElement.querySelectorAll('.page').length : 0) || 52;
  let currentMode = 'flipbook'; // 'flipbook' | 'gazette'
  let isMuted = localStorage.getItem('vce_audio_muted') === 'true';
  let zoomScale = 1.0;
  let isPanning = false;
  let startPanX = 0, startPanY = 0;
  let currentPanX = 0, currentPanY = 0;
  let audioCtx = null;

  if (audioIcon) {
    audioIcon.textContent = isMuted ? '🔇' : '🔊';
  }

  // --- Web Audio API Paper Rustle Synthesizer ---
  function initAudioContext() {
    if (!audioCtx) {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (AudioContextClass) {
        audioCtx = new AudioContextClass();
      }
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
  }

  function playPageTurnSound() {
    if (isMuted) return;
    try {
      initAudioContext();
      if (!audioCtx) return;

      const duration = 0.22;
      const sampleRate = audioCtx.sampleRate;
      const frameCount = Math.floor(sampleRate * duration);
      const buffer = audioCtx.createBuffer(1, frameCount, sampleRate);
      const data = buffer.getChannelData(0);

      // Synthesize realistic paper rustle with filtered decaying noise
      for (let i = 0; i < frameCount; i++) {
        const decay = Math.exp(-i / (frameCount * 0.28));
        data[i] = (Math.random() * 2 - 1) * decay;
      }

      const noiseSource = audioCtx.createBufferSource();
      noiseSource.buffer = buffer;

      // Bandpass filter to match tactile paper frequency range (~1400Hz)
      const bandpass = audioCtx.createBiquadFilter();
      bandpass.type = 'bandpass';
      bandpass.frequency.setValueAtTime(1400, audioCtx.currentTime);
      bandpass.Q.setValueAtTime(1.8, audioCtx.currentTime);

      const gainNode = audioCtx.createGain();
      gainNode.gain.setValueAtTime(0.01, audioCtx.currentTime);
      gainNode.gain.linearRampToValueAtTime(0.35, audioCtx.currentTime + 0.03);
      gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);

      noiseSource.connect(bandpass);
      bandpass.connect(gainNode);
      gainNode.connect(audioCtx.destination);

      noiseSource.start();
    } catch (err) {
      // Audio graceful fallback
    }
  }

  function playWelcomeChime() {
    if (isMuted) return;
    try {
      initAudioContext();
      if (!audioCtx) return;

      const freqs = [392, 523.25, 659.25, 783.99]; // G4, C5, E5, G5 (Harmonious chord)
      freqs.forEach((freq, idx) => {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime + idx * 0.08);

        gain.gain.setValueAtTime(0.001, audioCtx.currentTime + idx * 0.08);
        gain.gain.linearRampToValueAtTime(0.12, audioCtx.currentTime + idx * 0.08 + 0.04);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + idx * 0.08 + 0.9);

        osc.connect(gain);
        gain.connect(audioCtx.destination);

        osc.start(audioCtx.currentTime + idx * 0.08);
        osc.stop(audioCtx.currentTime + idx * 0.08 + 0.95);
      });
    } catch (e) {
      // Audio fallback
    }
  }

  // --- Dynamic Dimension Calculator (Screen Filling & Viewport Maximized) ---
  function getBookDimensions() {
    const isMobile = window.innerWidth < 1024;
    
    if (isMobile) {
      // Mobile Single Page Portrait (Fills mobile viewport snugly)
      const availW = window.innerWidth - 8;
      const availH = window.innerHeight - 84; // Space between 44px top navbar and 40px bottom dock
      
      // Target width fills ~98% of available mobile width
      let targetW = Math.floor(availW * 0.98);
      let targetH = Math.floor(targetW * 1.414);
      
      if (targetH > Math.floor(availH * 0.97)) {
        targetH = Math.floor(availH * 0.97);
        targetW = Math.floor(targetH / 1.414);
      }
      
      return { 
        width: Math.max(targetW, 280), 
        height: Math.max(targetH, 400), 
        isPortrait: true 
      };
    } else {
      // Desktop Two-Page Spread (Fills viewport snugly without dead space)
      const availW = window.innerWidth - 24; // Minimal side clearance for nav arrows
      const availH = window.innerHeight - 86; // Space between top navbar and bottom dock
      
      // Target height utilizes 97% of availH to eliminate dead vertical space!
      let targetH = Math.floor(availH * 0.97);
      // Classic magazine ratio 1 : 1.414 (A4)
      let pageW = Math.floor(targetH / 1.414);
      
      // Ensure spread fits width
      if (pageW * 2 > availW * 0.97) {
        pageW = Math.floor((availW * 0.97) / 2);
        targetH = Math.floor(pageW * 1.414);
      }
      
      return { 
        width: Math.max(pageW, 360), 
        height: Math.max(targetH, 520), 
        isPortrait: false 
      };
    }
  }

  // --- Trigger Editorial Animation on Page Turn ---
  function triggerPageAnimation(pageNum) {
    if (currentMode === 'flipbook') {
      window.scrollTo(0, 0);
    }
    const allPages = document.querySelectorAll('.page');
    allPages.forEach(p => {
      p.classList.remove('page-active');
      const content = p.querySelector('.page-content');
      if (content) content.scrollTop = 0;
    });

    const isSpread = pageFlip && pageFlip.getOrientation() === 'landscape' && pageNum > 1 && pageNum < totalPages;
    if (isSpread) {
      const leftNum = (pageNum % 2 === 0) ? pageNum : pageNum - 1;
      const rightNum = leftNum + 1;
      const pLeft = document.getElementById(`p${leftNum}`);
      const pRight = document.getElementById(`p${rightNum}`);
      if (pLeft) pLeft.classList.add('page-active');
      if (pRight) pRight.classList.add('page-active');
    } else {
      const pSingle = document.getElementById(`p${pageNum}`);
      if (pSingle) pSingle.classList.add('page-active');
    }
  }

  // --- Initialize St.PageFlip ---
  function initPageFlip() {
    const PageFlipConstructor = (window.St && window.St.PageFlip) ? window.St.PageFlip : null;
    if (!PageFlipConstructor) {
      console.warn("St.PageFlip library not detected. Falling back to Gazette view.");
      switchToGazetteMode();
      return;
    }

    const { width, height, isPortrait } = getBookDimensions();

    try {
      if (pageFlip) {
        pageFlip.destroy();
        pageFlip = null;
      }

      // Check if #flipbook element was removed from DOM by destroy() and restore it
      let flipEl = document.getElementById('flipbook');
      if (!flipEl) {
        flipEl = document.createElement('div');
        flipEl.id = 'flipbook';
        flipEl.className = 'st-flipbook';
        flipEl.innerHTML = originalFlipbookHTML;
        flipbookViewport.appendChild(flipEl);
      }

      pageFlip = new PageFlipConstructor(flipEl, {
        width: width,
        height: height,
        size: 'fixed', // 'fixed' ensures crisp pixel alignment and prevents DOM rendering collapse
        minWidth: 280,
        maxWidth: 1600,
        minHeight: 400,
        maxHeight: 2200,
        maxShadowOpacity: 0.5,
        showCover: true,
        mobileScrollSupport: true,
        usePortrait: isPortrait,
        startPage: Math.max(0, currentPage - 1),
        drawShadow: true,
        flippingTime: 750,
        useMouseEvents: true,
        clickEventForward: true
      });

      const pages = flipEl.querySelectorAll('.page');
      pageFlip.loadFromHTML(pages);

      pageFlip.on('flip', (e) => {
        currentPage = e.data + 1;
        updateUI(currentPage);
        triggerPageAnimation(currentPage);
        playPageTurnSound();
      });

      pageFlip.on('init', (e) => {
        updateUI(currentPage);
        triggerPageAnimation(currentPage);
      });

    } catch (err) {
      console.error("Error initializing PageFlip:", err);
    }
  }

  // --- Synchronize UI Elements ---
  function updateUI(pageNum) {
    if (currentMode === 'flipbook') {
      window.scrollTo(0, 0);
    }

    if (pageIndicator) {
      if (pageFlip && pageFlip.getOrientation() === 'landscape' && pageNum > 1 && pageNum < totalPages) {
        const leftPage = (pageNum % 2 === 0) ? pageNum : pageNum - 1;
        const rightPage = leftPage + 1;
        pageIndicator.textContent = `Pages ${leftPage}-${rightPage} of ${totalPages}`;
      } else {
        pageIndicator.textContent = `Page ${pageNum} of ${totalPages}`;
      }
    }

    if (pageScrubber) {
      pageScrubber.max = totalPages;
      pageScrubber.value = pageNum;
    }

    if (btnPrev) btnPrev.disabled = (pageNum <= 1);
    if (btnNext) btnNext.disabled = (pageNum >= totalPages);
    if (btnDockPrev) btnDockPrev.disabled = (pageNum <= 1);
    if (btnDockNext) btnDockNext.disabled = (pageNum >= totalPages);

    document.querySelectorAll('.thumb-card').forEach(card => {
      const cardPage = parseInt(card.dataset.page, 10);
      if (cardPage === pageNum) {
        card.classList.add('active');
        // Only scroll the horizontal thumbnail track internally if the thumbnail drawer is open
        // Never call card.scrollIntoView which causes the browser window to scroll down
        if (thumbnailStrip && thumbnailStrip.classList.contains('open') && thumbTrack) {
          const scrollLeft = card.offsetLeft - (thumbTrack.clientWidth / 2) + (card.clientWidth / 2);
          thumbTrack.scrollTo({ left: scrollLeft, behavior: 'smooth' });
        }
      } else {
        card.classList.remove('active');
      }
    });

    document.querySelectorAll('.toc-item').forEach(item => {
      const itemPage = parseInt(item.dataset.page, 10);
      if (itemPage === pageNum) {
        item.style.background = 'rgba(212, 175, 55, 0.2)';
      } else {
        item.style.background = '';
      }
    });
  }

  // --- Page Navigation Functions ---
  function goToPage(targetPage) {
    targetPage = Math.max(1, Math.min(totalPages, targetPage));
    if (currentMode === 'flipbook' && pageFlip) {
      window.scrollTo(0, 0);
      pageFlip.flip(targetPage - 1);
    } else {
      currentPage = targetPage;
      updateUI(currentPage);
      const articleEl = document.getElementById(`gazette-p${targetPage}`);
      if (articleEl) {
        articleEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  }

  function turnNext() {
    if (currentMode === 'flipbook' && pageFlip) {
      pageFlip.flipNext();
    } else {
      goToPage(currentPage + 1);
    }
  }

  function turnPrev() {
    if (currentMode === 'flipbook' && pageFlip) {
      pageFlip.flipPrev();
    } else {
      goToPage(currentPage - 1);
    }
  }

  if (btnPrev) btnPrev.addEventListener('click', turnPrev);
  if (btnNext) btnNext.addEventListener('click', turnNext);
  if (btnDockPrev) btnDockPrev.addEventListener('click', turnPrev);
  if (btnDockNext) btnDockNext.addEventListener('click', turnNext);

  if (pageScrubber) {
    pageScrubber.addEventListener('input', (e) => {
      const val = parseInt(e.target.value, 10);
      goToPage(val);
    });
  }

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {
    if (document.activeElement === gazetteSearchInput) return;

    if (e.key === 'ArrowRight' || e.key === 'PageDown') {
      turnNext();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
      turnPrev();
    } else if (e.key === 'Home') {
      goToPage(1);
    } else if (e.key === 'End') {
      goToPage(totalPages);
    } else if (e.key === 'Escape') {
      closeAllModals();
    }
  });

  // --- Mode Switching: Flipbook vs Gazette ---
  function switchToGazetteMode() {
    currentMode = 'gazette';
    flipbookContainer.classList.add('hidden-mode');
    gazetteContainer.classList.add('active-mode');
    if (modeLabel) modeLabel.textContent = 'Flipbook View';
    btnModeToggle.classList.add('active');

    setTimeout(() => {
      const articleEl = document.getElementById(`gazette-p${currentPage}`);
      if (articleEl) {
        articleEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 100);
  }

  function switchToFlipbookMode() {
    currentMode = 'flipbook';
    gazetteContainer.classList.remove('active-mode');
    flipbookContainer.classList.remove('hidden-mode');
    if (modeLabel) modeLabel.textContent = 'Gazette View';
    btnModeToggle.classList.remove('active');

    if (!pageFlip) {
      initPageFlip();
    } else {
      pageFlip.update();
      pageFlip.flip(currentPage - 1);
    }
    triggerPageAnimation(currentPage);
  }

  if (btnModeToggle) {
    btnModeToggle.addEventListener('click', () => {
      if (currentMode === 'flipbook') {
        switchToGazetteMode();
      } else {
        switchToFlipbookMode();
      }
    });
  }

  document.querySelectorAll('.btn-jump-to-flip').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const p = parseInt(btn.dataset.jump, 10);
      currentPage = p;
      switchToFlipbookMode();
      if (pageFlip) {
        pageFlip.flip(currentPage - 1);
      }
    });
  });

  // --- Drawer & Modal Handling ---
  function openToc() {
    tocDrawer.classList.add('open');
    modalBackdrop.classList.add('open');
  }

  function closeToc() {
    tocDrawer.classList.remove('open');
    modalBackdrop.classList.remove('open');
  }

  function toggleThumbs() {
    thumbnailStrip.classList.toggle('open');
  }

  function closeAllModals() {
    closeToc();
    thumbnailStrip.classList.remove('open');
    if (lightboxModal) lightboxModal.classList.remove('open');
  }

  if (btnToc) btnToc.addEventListener('click', openToc);
  if (btnDockToc) btnDockToc.addEventListener('click', openToc);
  if (btnTocClose) btnTocClose.addEventListener('click', closeToc);
  if (modalBackdrop) modalBackdrop.addEventListener('click', closeAllModals);
  if (btnToggleThumbs) btnToggleThumbs.addEventListener('click', toggleThumbs);

  document.querySelectorAll('.toc-item').forEach(item => {
    item.addEventListener('click', () => {
      const p = parseInt(item.dataset.page, 10);
      goToPage(p);
      closeToc();
    });
  });

  const thumbTrack = document.getElementById('thumb-track');
  if (thumbTrack && thumbTrack.children.length === 0) {
    for (let i = 1; i <= totalPages; i++) {
      const card = document.createElement('div');
      card.className = 'thumb-card';
      card.dataset.page = i;
      card.innerHTML = `<span class="thumb-page-num">P.${i}</span>`;
      card.addEventListener('click', () => {
        goToPage(i);
        if (thumbnailStrip) thumbnailStrip.classList.remove('open');
      });
      thumbTrack.appendChild(card);
    }
  }


  // --- Zoom & Pan Engine for Flipbook ---
  function updateZoom() {
    if (zoomLevelDisplay) {
      zoomLevelDisplay.textContent = `${Math.round(zoomScale * 100)}%`;
    }
    if (flipbookViewport) {
      flipbookViewport.style.transform = `scale(${zoomScale}) translate(${currentPanX}px, ${currentPanY}px)`;
      if (zoomScale > 1.0) {
        flipbookViewport.style.cursor = 'grab';
      } else {
        flipbookViewport.style.cursor = 'default';
        currentPanX = 0;
        currentPanY = 0;
      }
    }
  }

  if (btnZoomIn) {
    btnZoomIn.addEventListener('click', () => {
      zoomScale = Math.min(zoomScale + 0.25, 2.2);
      updateZoom();
    });
  }

  if (btnZoomOut) {
    btnZoomOut.addEventListener('click', () => {
      zoomScale = Math.max(zoomScale - 0.25, 1.0);
      if (zoomScale === 1.0) {
        currentPanX = 0;
        currentPanY = 0;
      }
      updateZoom();
    });
  }

  if (btnZoomReset) {
    btnZoomReset.addEventListener('click', () => {
      zoomScale = 1.0;
      currentPanX = 0;
      currentPanY = 0;
      updateZoom();
    });
  }

  if (flipbookViewport) {
    flipbookViewport.addEventListener('mousedown', (e) => {
      if (zoomScale <= 1.0) return;
      isPanning = true;
      startPanX = e.clientX - currentPanX;
      startPanY = e.clientY - currentPanY;
      flipbookViewport.style.cursor = 'grabbing';
    });

    window.addEventListener('mousemove', (e) => {
      if (!isPanning || zoomScale <= 1.0) return;
      currentPanX = e.clientX - startPanX;
      currentPanY = e.clientY - startPanY;
      updateZoom();
    });

    window.addEventListener('mouseup', () => {
      if (isPanning) {
        isPanning = false;
        if (flipbookViewport) {
          flipbookViewport.style.cursor = (zoomScale > 1.0) ? 'grab' : 'default';
        }
      }
    });
  }

  // --- Fullscreen Poster & Broadside Viewer with Dynamic Event Details ---
  let currentEventPage = null;

  function extractEventData(sourceFrame) {
    if (!sourceFrame) return null;
    let container = sourceFrame.closest('.page') || sourceFrame.closest('.gazette-section') || sourceFrame.closest('article');
    if (!container) return null;

    // If source is a poster page or spread page without extensive text, check the facing page for full event story
    if (container.classList && (container.classList.contains('poster-page') || container.classList.contains('spread-page'))) {
      const pageId = container.id;
      if (pageId && pageId.startsWith('p')) {
        const pNum = parseInt(pageId.substring(1), 10);
        const facingNum = (pNum % 2 === 0) ? (pNum + 1) : (pNum - 1);
        const facingPage = document.getElementById(`p${facingNum}`);
        if (facingPage && facingPage.querySelector('.headline-lead, .headline-section, .editorial-cols')) {
          container = facingPage;
        }
      }
    }

    let pageNum = container.dataset.page;
    if (!pageNum && container.id) {
      const match = container.id.match(/\d+/);
      if (match) pageNum = match[0];
    }
    if (!pageNum) {
      const pageNumEl = container.querySelector('.page-num');
      if (pageNumEl) {
        const match = pageNumEl.textContent.match(/\d+/);
        if (match) pageNum = match[0];
      }
    }

    let dept = '';
    const deptEl = container.querySelector('.page-header-title') ||
                   container.querySelector('.headline-section span:first-child') ||
                   container.querySelector('.gazette-section-kicker');
    if (deptEl) dept = deptEl.textContent.trim();

    let dateText = '';
    const dateEl = container.querySelector('.headline-tag') ||
                   container.querySelector('.byline-date') ||
                   container.querySelector('.gazette-section-date');
    if (dateEl) dateText = dateEl.textContent.trim();

    let headline = '';
    const headlineEl = container.querySelector('.headline-lead') ||
                       container.querySelector('.page-masthead-title') ||
                       container.querySelector('h2') ||
                       container.querySelector('h1') ||
                       container.querySelector('h3');
    if (headlineEl) headline = headlineEl.textContent.trim();

    let byline = '';
    const bylineEl = container.querySelector('.byline-bar') ||
                     container.querySelector('.page-dateline');
    if (bylineEl) byline = bylineEl.textContent.trim();

    let bodyHTML = '';
    const editorialCols = container.querySelector('.editorial-cols');
    if (editorialCols) {
      editorialCols.querySelectorAll('p').forEach(p => {
        bodyHTML += `<p>${p.innerHTML}</p>`;
      });
    } else {
      container.querySelectorAll('p').forEach(p => {
        if (!p.closest('.news-caption') && !p.closest('.lightbox-content-container') && !p.closest('.page-footer')) {
          bodyHTML += `<p>${p.innerHTML}</p>`;
        }
      });
    }

    const extraBlocks = container.querySelectorAll('.editorial-card, .takeaways-box, .news-table-wrapper, .pull-quote');
    extraBlocks.forEach(block => {
      if (!block.closest('.editorial-cols')) {
        bodyHTML += block.outerHTML;
      }
    });

    return {
      page: pageNum ? parseInt(pageNum, 10) : null,
      dept: dept || "VAIGAI'S IKIGAI GAZETTE",
      date: dateText || "ACADEMIC ARCHIVES 2026",
      headline: headline || "CAMPUS BROADCAST",
      byline: byline || "",
      bodyHTML: bodyHTML || "<p>Detailed editorial story available in the publication.</p>"
    };
  }

  function setLightboxView(view) {
    if (!lightboxModal) return;
    lightboxModal.dataset.view = view;
    if (view === 'details') {
      if (lightboxToggleInfo) lightboxToggleInfo.classList.add('active');
      if (lightboxInfoBtnLabel) lightboxInfoBtnLabel.textContent = 'Fullscreen Poster';
      if (lightboxCaptionHint) {
        lightboxCaptionHint.innerHTML = '<span>⛶ Click to expand fullscreen poster</span><span>▴</span>';
      }
    } else {
      if (lightboxToggleInfo) lightboxToggleInfo.classList.remove('active');
      if (lightboxInfoBtnLabel) lightboxInfoBtnLabel.textContent = 'Event Details';
      if (lightboxCaptionHint) {
        lightboxCaptionHint.innerHTML = '<span>ℹ️ Click to read the full event story & details</span><span>▾</span>';
      }
    }
  }

  function toggleLightboxView() {
    if (!lightboxModal) return;
    const currentView = lightboxModal.dataset.view || 'poster';
    setLightboxView(currentView === 'poster' ? 'details' : 'poster');
  }

  function openLightbox(imgSrc, captionText, sourceFrame) {
    if (!lightboxModal) return;
    lightboxImg.src = imgSrc;
    lightboxCaption.textContent = captionText || '';

    const eventData = extractEventData(sourceFrame);
    if (eventData) {
      currentEventPage = eventData.page;
      if (lightboxEventTag) {
        lightboxEventTag.textContent = `${eventData.dept} • ${eventData.date}`;
      }
      if (lightboxInfoDept) {
        lightboxInfoDept.textContent = eventData.dept;
      }
      if (lightboxInfoDate) {
        lightboxInfoDate.textContent = eventData.date;
      }
      if (lightboxInfoTitle) {
        lightboxInfoTitle.textContent = eventData.headline;
      }
      if (lightboxInfoByline) {
        lightboxInfoByline.textContent = eventData.byline;
        lightboxInfoByline.style.display = eventData.byline ? 'flex' : 'none';
      }
      if (lightboxInfoBody) {
        lightboxInfoBody.innerHTML = eventData.bodyHTML;
      }
      if (lightboxJumpPage) {
        lightboxJumpPage.style.display = currentEventPage ? 'inline-flex' : 'none';
        const jumpText = lightboxJumpPage.querySelector('.btn-text');
        if (jumpText && currentEventPage) {
          jumpText.textContent = `Page ${currentEventPage}`;
        }
      }
    } else {
      currentEventPage = null;
      if (lightboxEventTag) lightboxEventTag.textContent = 'VAIGAI ARCHIVAL POSTER';
      if (lightboxInfoDept) lightboxInfoDept.textContent = "VAIGAI'S IKIGAI";
      if (lightboxInfoDate) lightboxInfoDate.textContent = 'SPECIAL EDITION';
      if (lightboxInfoTitle) lightboxInfoTitle.textContent = captionText || 'Archival Broadside';
      if (lightboxInfoByline) lightboxInfoByline.style.display = 'none';
      if (lightboxInfoBody) lightboxInfoBody.innerHTML = `<p>${captionText || 'Archival image from Vaigai College of Engineering publication.'}</p>`;
      if (lightboxJumpPage) lightboxJumpPage.style.display = 'none';
    }

    // Default to scaled fullscreen portrait poster view
    setLightboxView('poster');
    lightboxModal.classList.add('open');
  }

  // Lightbox Image Rotation Support (e.g. for vertical mobile screen users)
  const lightboxRotateBtn = document.getElementById('lightbox-rotate-btn');
  let lightboxRotationDeg = 0;
  if (lightboxRotateBtn) {
    lightboxRotateBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      lightboxRotationDeg = (lightboxRotationDeg + 90) % 360;
      if (lightboxImg) {
        lightboxImg.style.transform = `rotate(${lightboxRotationDeg}deg)`;
      }
    });
  }

  // Mobile Spread Container Rotation Toggle
  document.querySelectorAll('.mobile-spread-rotate-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const container = btn.closest('.spread-container');
      if (container) {
        container.classList.toggle('mobile-rotated');
      }
    });
  });

  if (lightboxToggleInfo) {
    lightboxToggleInfo.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleLightboxView();
    });
  }

  if (lightboxCaptionHint) {
    lightboxCaptionHint.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleLightboxView();
    });
  }

  if (lightboxImgFrame) {
    lightboxImgFrame.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleLightboxView();
    });
  }

  if (lightboxJumpPage) {
    lightboxJumpPage.addEventListener('click', (e) => {
      e.stopPropagation();
      if (currentEventPage) {
        lightboxModal.classList.remove('open');
        goToPage(currentEventPage);
      }
    });
  }

  if (lightboxClose) {
    lightboxClose.addEventListener('click', () => {
      lightboxModal.classList.remove('open');
    });
  }

  if (lightboxModal) {
    lightboxModal.addEventListener('click', (e) => {
      if (e.target === lightboxModal || e.target === lightboxContentContainer) {
        lightboxModal.classList.remove('open');
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightboxModal && lightboxModal.classList.contains('open')) {
      lightboxModal.classList.remove('open');
    }
  });

  // Images act as seamless parts of the publication page — clicks turn pages without lightbox expansion


  // --- Audio Mute Toggle ---
  if (btnAudio) {
    btnAudio.addEventListener('click', () => {
      isMuted = !isMuted;
      localStorage.setItem('vce_audio_muted', isMuted);
      if (audioIcon) {
        audioIcon.textContent = isMuted ? '🔇' : '🔊';
      }
      if (!isMuted) {
        initAudioContext();
        playPageTurnSound();
      }
    });
  }

  // --- Theme Selection ---
  if (themeSelect) {
    const savedTheme = localStorage.getItem('vce_theme') || 'newsprint';
    themeSelect.value = savedTheme;
    document.body.setAttribute('data-theme', savedTheme);

    themeSelect.addEventListener('change', (e) => {
      const newTheme = e.target.value;
      document.body.setAttribute('data-theme', newTheme);
      localStorage.setItem('vce_theme', newTheme);
    });
  }

  // --- Fullscreen Toggle ---
  if (btnFullscreen) {
    btnFullscreen.addEventListener('click', () => {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen().catch(() => {});
        }
      }
    });
  }

  // --- Search Bar in Gazette Mode ---
  if (gazetteSearchInput) {
    gazetteSearchInput.addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase().trim();
      document.querySelectorAll('.gazette-section').forEach(section => {
        if (!query) {
          section.style.display = 'block';
        } else {
          const text = section.textContent.toLowerCase();
          section.style.display = text.includes(query) ? 'block' : 'none';
        }
      });
    });
  }

  // --- Print Publication ---
  if (btnPrint) {
    btnPrint.addEventListener('click', () => {
      switchToGazetteMode();
      setTimeout(() => {
        window.print();
      }, 350);
    });
  }

  if (brandLink) {
    brandLink.addEventListener('click', () => {
      goToPage(1);
    });
  }

  // --- Responsive Resize Handler (Android URL Bar & Orientation Optimized) ---
  let lastWidth = window.innerWidth;
  let lastPortrait = window.innerWidth < 1024;
  let resizeTimeout = null;

  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      const currentWidth = window.innerWidth;
      const currentPortrait = currentWidth < 1024;
      
      // Only re-initialize if orientation mode changed or screen width changed substantially (> 50px)
      // This prevents Android Chrome URL bar toggles from flickering or resetting the flipbook!
      if (currentPortrait !== lastPortrait || Math.abs(currentWidth - lastWidth) > 50) {
        lastWidth = currentWidth;
        lastPortrait = currentPortrait;
        if (currentMode === 'flipbook') {
          initPageFlip();
        }
      }
    }, 250);
  });

  // --- Startup ---
  initPageFlip();
  updateUI(currentPage);
  triggerPageAnimation(currentPage);
});
