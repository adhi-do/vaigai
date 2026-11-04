/**
 * VAIGAI'S IKIGAI — Interactive Newspaper & Book Publication
 * High-End Heyzine-Inspired Viewer Engine
 * Includes Proportional Aspect Ratio, Web Audio Synthesis, Responsive Sizing & Dual Modes
 */

document.addEventListener('DOMContentLoaded', () => {
  // --- DOM Elements ---
  const splash = document.getElementById('pretext-splash');
  const btnEnterSplash = document.getElementById('btn-enter-splash');
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
  const thumbnailStrip = document.getElementById('thumbnail-strip');
  
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
  const lightboxCaption = document.getElementById('lightbox-caption');
  const lightboxClose = document.getElementById('lightbox-close');
  
  const gazetteSearchInput = document.getElementById('gazette-search-input');
  
  // --- State Variables ---
  let pageFlip = null;
  let currentPage = 1;
  const totalPages = 38;
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

  // --- Dynamic Dimension Calculator (Heyzine Proportional Sizing & Android Optimized) ---
  function getBookDimensions() {
    const isMobile = window.innerWidth < 1024;
    
    if (isMobile) {
      // Mobile Single Page Portrait (Android & iPhone Touchscreen Optimized)
      const availW = window.innerWidth - 16;
      const availH = window.innerHeight - 88; // Space between 44px top navbar and 40px bottom dock
      
      // Target width fills ~96% of screen width (capped at 520px)
      let targetW = Math.min(availW, 520);
      
      // Classic magazine ratio ~ 1 : 1.414 (A4)
      let targetH = Math.floor(targetW * 1.414);
      // Ensure comfortable vertical clearance so top and bottom edges are never clipped!
      if (targetH > Math.floor(availH * 0.90)) {
        targetH = Math.floor(availH * 0.90);
        targetW = Math.floor(targetH / 1.414);
      }
      
      return { 
        width: Math.max(targetW, 280), 
        height: Math.max(targetH, 400), 
        isPortrait: true 
      };
    } else {
      // Desktop Two-Page Spread (Heyzine Proportions)
      const availW = window.innerWidth - 60; // 30px breathing space on each side
      const availH = window.innerHeight - 96; // Space between navbar and bottom dock
      
      // Target height: 86% of availH leaves ~35px-45px vertical clearance so the top and curling corners are NEVER cut!
      let targetH = Math.min(Math.floor(availH * 0.86), 740);
      // Classic magazine width-to-height ratio 1 : 1.38
      let pageW = Math.floor(targetH / 1.38);
      
      // Ensure spread fits width
      if (pageW * 2 > availW * 0.94) {
        pageW = Math.floor((availW * 0.94) / 2);
        targetH = Math.floor(pageW * 1.38);
      }
      
      return { 
        width: Math.max(pageW, 320), 
        height: Math.max(targetH, 500), 
        isPortrait: false 
      };
    }
  }

  // --- Trigger Editorial Animation on Page Turn ---
  function triggerPageAnimation(pageNum) {
    const allPages = document.querySelectorAll('.page');
    allPages.forEach(p => p.classList.remove('page-active'));

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
        maxWidth: 750,
        minHeight: 400,
        maxHeight: 1050,
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
        card.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
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

  document.querySelectorAll('.thumb-card').forEach(card => {
    card.addEventListener('click', () => {
      const p = parseInt(card.dataset.page, 10);
      goToPage(p);
      thumbnailStrip.classList.remove('open');
    });
  });

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

  // --- Lightbox Image Inspection ---
  function openLightbox(imgSrc, captionText) {
    if (!lightboxModal) return;
    lightboxImg.src = imgSrc;
    lightboxCaption.textContent = captionText || '';
    lightboxModal.classList.add('open');
  }

  if (lightboxClose) {
    lightboxClose.addEventListener('click', () => {
      lightboxModal.classList.remove('open');
    });
  }

  if (lightboxModal) {
    lightboxModal.addEventListener('click', (e) => {
      if (e.target === lightboxModal) {
        lightboxModal.classList.remove('open');
      }
    });
  }

  document.querySelectorAll('.news-image-frame, .vairamuthu-frame, .nptel-avatar').forEach(frame => {
    frame.addEventListener('click', (e) => {
      let img = frame.tagName === 'IMG' ? frame : frame.querySelector('img');
      let caption = frame.querySelector ? frame.querySelector('.news-caption') : null;
      if (img) {
        openLightbox(img.src, caption ? caption.textContent.trim() : (img.alt || 'Vaigai College Publication Photo'));
      }
    });
  });

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

  // --- Splash Screen Dismiss ---
  function dismissSplash() {
    if (splash && !splash.classList.contains('hidden')) {
      splash.classList.add('hidden');
      initAudioContext();
      playWelcomeChime();
      triggerPageAnimation(currentPage);
    }
  }

  if (btnEnterSplash) {
    btnEnterSplash.addEventListener('click', (e) => {
      e.stopPropagation();
      dismissSplash();
    });
  }

  if (splash) {
    splash.addEventListener('click', dismissSplash);
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

  // ==========================================================================
  // PRETEXT.JS ENGINE — REAL-TIME DYNAMIC ARITHMETIC TEXT REFLOW DEMO
  // (Direct reference to https://pretextjs.dev/ by Cheng Lou)
  // ==========================================================================
  const pretextCanvas = document.getElementById('pretext-splash-canvas');
  const pretextContainer = document.getElementById('splash-pretext-container');
  const pretextFpsEl = document.getElementById('pretext-fps');
  const pretextLinesEl = document.getElementById('pretext-lines');
  
  if (pretextContainer) {
    pretextContainer.addEventListener('click', (e) => {
      // Don't auto-dismiss splash when interacting with the Pretext demo
      e.stopPropagation();
    });
  }

  if (pretextCanvas && pretextCanvas.getContext) {
    const ctx = pretextCanvas.getContext('2d');
    const manifestoText = "What is Vaigai's Ikigai? The Vision that drives us. The Achievements that define us. The Intelligence that inspires us. The Greatness we nurture. The Academic aspirations we pursue. The Innovations through which we create impact. Where Purpose Meets Possibility.";
    const words = manifestoText.split(' ');
    
    // High-DPI Canvas scaling
    let dpr = window.devicePixelRatio || 1;
    let canvasW = 560;
    let canvasH = 155;
    
    function resizePretextCanvas() {
      if (!pretextCanvas) return;
      const rect = pretextCanvas.getBoundingClientRect();
      if (rect.width > 0) {
        canvasW = rect.width;
        canvasH = rect.height || 155;
        pretextCanvas.width = canvasW * dpr;
        pretextCanvas.height = canvasH * dpr;
        ctx.scale(dpr, dpr);
      }
    }
    resizePretextCanvas();

    // PHASE 1: PREPARE (One-time Canvas measurement & caching — Zero DOM reads)
    let cachedWords = [];
    let spaceWidth = 5;
    const fontStr = "500 14px 'Merriweather', Georgia, serif";

    function prepareWords() {
      ctx.font = fontStr;
      spaceWidth = ctx.measureText(' ').width;
      cachedWords = words.map(w => ({
        text: w,
        width: ctx.measureText(w).width,
        isTitle: w.includes('Vaigai') || w.includes('Ikigai') || w.includes('Purpose') || w.includes('Possibility')
      }));
    }
    prepareWords();

    // Obstacle tracking (Cursor interaction)
    let cursorX = -200;
    let cursorY = -200;
    let targetCursorX = -200;
    let targetCursorY = -200;
    let isMouseOver = false;
    let obstacleRadius = 38;
    let autoTime = 0;

    pretextCanvas.addEventListener('mousemove', (e) => {
      const rect = pretextCanvas.getBoundingClientRect();
      targetCursorX = e.clientX - rect.left;
      targetCursorY = e.clientY - rect.top;
      isMouseOver = true;
    });

    pretextCanvas.addEventListener('mouseleave', () => {
      isMouseOver = false;
    });

    // Touch support for Android mobile users
    pretextCanvas.addEventListener('touchmove', (e) => {
      if (e.touches && e.touches[0]) {
        const rect = pretextCanvas.getBoundingClientRect();
        targetCursorX = e.touches[0].clientX - rect.left;
        targetCursorY = e.touches[0].clientY - rect.top;
        isMouseOver = true;
      }
    }, { passive: true });

    pretextCanvas.addEventListener('touchend', () => {
      isMouseOver = false;
    });

    // FPS Counter metrics
    let lastFrameTime = performance.now();
    let frameCount = 0;
    let fpsTimer = 0;

    // PHASE 2: HOT-PATH REAL-TIME ARITHMETIC REFLOW (60 FPS Pure Math Layout)
    function renderPretextFrame(now) {
      if (!splash || splash.classList.contains('hidden')) {
        // Stop animation loop once splash is closed to save battery/CPU
        return;
      }

      const delta = (now - lastFrameTime) / 1000;
      lastFrameTime = now;
      frameCount++;
      fpsTimer += delta;
      if (fpsTimer >= 0.5) {
        const currentFps = Math.round(frameCount / fpsTimer);
        if (pretextFpsEl) pretextFpsEl.textContent = `⚡ ${currentFps} FPS Layout`;
        frameCount = 0;
        fpsTimer = 0;
      }

      // Smooth cursor lerp or idle gentle wandering
      if (isMouseOver) {
        cursorX += (targetCursorX - cursorX) * 0.22;
        cursorY += (targetCursorY - cursorY) * 0.22;
      } else {
        autoTime += 0.025;
        // Gentle figure-8 wandering in center
        cursorX = (canvasW / 2) + Math.sin(autoTime) * (canvasW * 0.22);
        cursorY = (canvasH / 2) + Math.cos(autoTime * 1.5) * 26;
      }

      ctx.clearRect(0, 0, canvasW, canvasH);

      // Draw subtle glowing Pretext cursor obstacle orb
      const grad = ctx.createRadialGradient(cursorX, cursorY, 0, cursorX, cursorY, obstacleRadius);
      grad.addColorStop(0, 'rgba(212, 175, 55, 0.45)');
      grad.addColorStop(0.5, 'rgba(212, 175, 55, 0.18)');
      grad.addColorStop(1, 'rgba(212, 175, 55, 0)');
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(cursorX, cursorY, obstacleRadius, 0, Math.PI * 2);
      ctx.fill();

      // Subtle ring
      ctx.strokeStyle = 'rgba(212, 175, 55, 0.35)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.arc(cursorX, cursorY, obstacleRadius * 0.8, 0, Math.PI * 2);
      ctx.stroke();

      // Dynamic line-by-line reflow calculation
      ctx.font = fontStr;
      const padding = 12;
      const lineH = 26;
      let y = 24;
      let wordIdx = 0;
      let lineCount = 0;

      while (wordIdx < cachedWords.length && y < canvasH + 10) {
        lineCount++;
        const dy = Math.abs(y - 6 - cursorY);
        
        if (dy < obstacleRadius) {
          // Obstacle cuts through this line! Compute available left/right corridors
          const dx = Math.sqrt(obstacleRadius * obstacleRadius - dy * dy) + 12;
          const leftStart = padding;
          const leftEnd = Math.max(leftStart, cursorX - dx);
          const rightStart = Math.min(canvasW - padding, cursorX + dx);
          const rightEnd = canvasW - padding;

          const leftCorridor = leftEnd - leftStart;
          const rightCorridor = rightEnd - rightStart;

          // Fill left corridor if wide enough
          if (leftCorridor > 60) {
            let curX = leftStart;
            while (wordIdx < cachedWords.length) {
              const item = cachedWords[wordIdx];
              if (curX + item.width <= leftEnd) {
                ctx.fillStyle = item.isTitle ? '#fbbf24' : '#e2e8f0';
                ctx.fillText(item.text, curX, y);
                curX += item.width + spaceWidth;
                wordIdx++;
              } else {
                break;
              }
            }
          }

          // Fill right corridor if wide enough
          if (rightCorridor > 60) {
            let curX = rightStart;
            while (wordIdx < cachedWords.length) {
              const item = cachedWords[wordIdx];
              if (curX + item.width <= rightEnd) {
                ctx.fillStyle = item.isTitle ? '#fbbf24' : '#e2e8f0';
                ctx.fillText(item.text, curX, y);
                curX += item.width + spaceWidth;
                wordIdx++;
              } else {
                break;
              }
            }
          }
        } else {
          // Unobstructed full-width line
          const maxW = canvasW - padding * 2;
          let curX = padding;
          while (wordIdx < cachedWords.length) {
            const item = cachedWords[wordIdx];
            if (curX + item.width <= maxW + padding) {
              ctx.fillStyle = item.isTitle ? '#fbbf24' : '#e2e8f0';
              ctx.fillText(item.text, curX, y);
              curX += item.width + spaceWidth;
              wordIdx++;
            } else {
              break;
            }
          }
        }
        y += lineH;
      }

      if (pretextLinesEl) pretextLinesEl.textContent = `Line Count: ${lineCount}`;
      requestAnimationFrame(renderPretextFrame);
    }

    requestAnimationFrame(renderPretextFrame);
    window.addEventListener('resize', () => {
      resizePretextCanvas();
      prepareWords();
    });
  }

  // ==========================================================================
  // PRETEXT EDITORIAL READING SPOTLIGHT (Interactive Desktop Cursor Luminary)
  // ==========================================================================
  const cursorLens = document.getElementById('pretext-cursor-lens');
  if (cursorLens) {
    let targetX = -100, targetY = -100;
    let currentX = -100, currentY = -100;
    let isLensActive = false;

    window.addEventListener('mousemove', (e) => {
      // Don't show lens when splash is active or on touch devices
      if (splash && !splash.classList.contains('hidden')) {
        cursorLens.classList.remove('active');
        return;
      }

      targetX = e.clientX;
      targetY = e.clientY;

      if (!isLensActive) {
        isLensActive = true;
        cursorLens.classList.add('active');
      }

      // Check if cursor is over editorial text or headings
      const target = e.target;
      const isText = target && (
        target.matches('p, h1, h2, h3, h4, .news-paragraph, .editorial-cols p, .pull-quote, .byline-bar, .page-header, .page-footer') ||
        target.closest('.editorial-cols, .news-paragraph, .pretext-card, .pull-quote')
      );
      
      const isImage = target && (
        target.matches('img, .news-img, .news-image-frame, .nptel-avatar, .vairamuthu-frame') ||
        target.closest('.news-image-frame, .vairamuthu-frame, .nptel-grid')
      );

      if (isImage) {
        // Keep images 100% clean, stable and unobscured
        cursorLens.classList.remove('active');
        cursorLens.classList.remove('focus-text');
      } else if (isText) {
        cursorLens.classList.add('active');
        cursorLens.classList.add('focus-text');
      } else {
        cursorLens.classList.add('active');
        cursorLens.classList.remove('focus-text');
      }
    });

    document.addEventListener('mouseleave', () => {
      isLensActive = false;
      cursorLens.classList.remove('active');
    });

    function renderLens() {
      if (isLensActive) {
        currentX += (targetX - currentX) * 0.25;
        currentY += (targetY - currentY) * 0.25;
        cursorLens.style.left = `${currentX}px`;
        cursorLens.style.top = `${currentY}px`;
      }
      requestAnimationFrame(renderLens);
    }
    requestAnimationFrame(renderLens);
  }

  // --- Startup ---
  initPageFlip();
  updateUI(currentPage);
  triggerPageAnimation(currentPage);
});
