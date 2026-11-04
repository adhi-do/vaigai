/**
 * VAIGAI'S IKIGAI — Interactive Newspaper & Book Publication
 * Full-Screen Immersive Heyzine-Inspired Viewer Engine
 * Includes Kinetic Editorial Motion, Web Audio Synthesis, Responsive Sizing & Dual Modes
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

  // --- Dynamic Screen-Filling Dimension Calculator (Heyzine Inspired) ---
  function getBookDimensions() {
    const isMobile = window.innerWidth < 1024;
    const availW = window.innerWidth - (isMobile ? 12 : 36);
    // Height available between 44px top navbar and 40px bottom dock
    const availH = window.innerHeight - 84;
    
    if (isMobile) {
      // Mobile Single Page Portrait: Fills ~95% width and height
      const targetW = Math.min(availW, 600);
      const targetH = Math.min(availH, targetW * 1.414);
      return { 
        width: Math.floor(targetW), 
        height: Math.floor(targetH), 
        isPortrait: true 
      };
    } else {
      // Desktop Two-Page Spread: Fills ~92% - 95% of viewport height
      let targetH = Math.floor(availH * 0.94);
      let pageW = Math.floor(targetH / 1.414);
      // Ensure two pages do not exceed available width
      if (pageW * 2 > availW * 0.96) {
        pageW = Math.floor((availW * 0.96) / 2);
        targetH = Math.floor(pageW * 1.414);
      }
      return { 
        width: Math.max(pageW, 380), 
        height: Math.max(targetH, 540), 
        isPortrait: false 
      };
    }
  }

  // --- Trigger Kinetic Editorial & Pretext Animation ---
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
      }

      pageFlip = new PageFlipConstructor(flipbookElement, {
        width: width,
        height: height,
        size: 'stretch',
        minWidth: 280,
        maxWidth: 800,
        minHeight: 400,
        maxHeight: 1100,
        maxShadowOpacity: 0.55,
        showCover: true,
        mobileScrollSupport: true,
        usePortrait: isPortrait,
        startPage: Math.max(0, currentPage - 1),
        drawShadow: true,
        flippingTime: 750,
        useMouseEvents: true,
        clickEventForward: true
      });

      const pages = document.querySelectorAll('.page');
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

  // --- Print Publication ---
  if (btnPrint) {
    btnPrint.addEventListener('click', () => {
      switchToGazetteMode();
      setTimeout(() => {
        window.print();
      }, 300);
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

  // --- Splash Screen Dismiss ---
  if (btnEnterSplash) {
    btnEnterSplash.addEventListener('click', () => {
      splash.classList.add('hidden');
      initAudioContext();
      playWelcomeChime();
      triggerPageAnimation(currentPage);
    });
  }

  if (brandLink) {
    brandLink.addEventListener('click', () => {
      goToPage(1);
    });
  }

  // --- Responsive Resize Handler ---
  let resizeTimeout = null;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      if (currentMode === 'flipbook' && pageFlip) {
        initPageFlip();
      }
    }, 250);
  });

  // --- Startup ---
  initPageFlip();
  updateUI(currentPage);
  triggerPageAnimation(currentPage);
});
