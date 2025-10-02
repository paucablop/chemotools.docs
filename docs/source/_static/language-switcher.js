// Language switcher for chemotools documentation
document.addEventListener('DOMContentLoaded', function() {
    // Create language switcher
    const langSwitcher = document.createElement('div');
    langSwitcher.className = 'language-switcher';
    langSwitcher.innerHTML = `
        <div class="dropdown">
            <button class="dropbtn" id="langBtn">
                <i class="fas fa-globe"></i> Language
            </button>
            <div class="dropdown-content">
                <a href="#" onclick="switchLanguage('en')">🇺🇸 English</a>
                <a href="#" onclick="switchLanguage('es')">🇪🇸 Español</a>
                <a href="#" onclick="switchLanguage('zh_CN')">🇨🇳 中文</a>
            </div>
        </div>
    `;

    // Insert into navbar
    const navbar = document.querySelector('.navbar-nav') || document.querySelector('.navbar');
    if (navbar) {
        navbar.appendChild(langSwitcher);
    }

    // Update button text based on current language
    updateLanguageButton();
});

function switchLanguage(lang) {
    const currentUrl = window.location.href;
    const currentPath = window.location.pathname;
    
    let newUrl;
    
    // Determine the base path and current language
    if (currentPath.includes('/es/')) {
        // Currently Spanish
        newUrl = currentUrl.replace('/es/', lang === 'en' ? '/' : `/${lang}/`);
    } else if (currentPath.includes('/zh_CN/')) {
        // Currently Chinese
        newUrl = currentUrl.replace('/zh_CN/', lang === 'en' ? '/' : `/${lang}/`);
    } else {
        // Currently English (default)
        if (lang === 'en') {
            newUrl = currentUrl; // Stay on English
        } else {
            // Add language prefix
            const baseUrl = currentUrl.split('/').slice(0, 3).join('/');
            const pathPart = currentUrl.split('/').slice(3).join('/');
            newUrl = `${baseUrl}/${lang}/${pathPart}`;
        }
    }
    
    window.location.href = newUrl;
}

function updateLanguageButton() {
    const currentPath = window.location.pathname;
    const langBtn = document.getElementById('langBtn');
    
    if (!langBtn) return;
    
    if (currentPath.includes('/es/')) {
        langBtn.innerHTML = '<i class="fas fa-globe"></i> 🇪🇸 Español';
    } else if (currentPath.includes('/zh_CN/')) {
        langBtn.innerHTML = '<i class="fas fa-globe"></i> 🇨🇳 中文';
    } else {
        langBtn.innerHTML = '<i class="fas fa-globe"></i> 🇺🇸 English';
    }
}
