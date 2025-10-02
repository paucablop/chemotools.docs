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
                <a href="#" onclick="switchLanguage('en')">English</a>
                <a href="#" onclick="switchLanguage('es')">Español</a>
                <a href="#" onclick="switchLanguage('zh_CN')">中文</a>
            </div>
        </div>
    `;

    // Insert into body (positioned with CSS)
    document.body.appendChild(langSwitcher);

    // Update button text based on current language
    updateLanguageButton();
});

function switchLanguage(lang) {
    const currentUrl = window.location.href;
    const currentPath = window.location.pathname;
    
    let newUrl;
    
    // Handle file:// URLs (for local development)
    if (currentUrl.startsWith('file://')) {
        // Get the directory path without the filename
        const urlParts = currentUrl.split('/');
        const filename = urlParts[urlParts.length - 1];
        const basePath = urlParts.slice(0, -1).join('/');
        
        if (currentPath.includes('/zh_CN/')) {
            // Currently Chinese - navigate to other languages
            if (lang === 'en') {
                // Go back to the English version by removing /zh_CN/ from the path
                newUrl = basePath.replace('/zh_CN', '') + '/' + filename;
            } else if (lang === 'es') {
                newUrl = basePath.replace('/zh_CN', '/es') + '/' + filename;
            } else {
                newUrl = currentUrl; // Stay on Chinese
            }
        } else if (currentPath.includes('/es/')) {
            // Currently Spanish - navigate to other languages
            if (lang === 'en') {
                // Go back to the English version by removing /es/ from the path
                newUrl = basePath.replace('/es', '') + '/' + filename;
            } else if (lang === 'zh_CN') {
                newUrl = basePath.replace('/es', '/zh_CN') + '/' + filename;
            } else {
                newUrl = currentUrl; // Stay on Spanish
            }
        } else {
            // Currently English - navigate to other languages
            if (lang === 'zh_CN') {
                newUrl = basePath + '/zh_CN/' + filename;
            } else if (lang === 'es') {
                newUrl = basePath + '/es/' + filename;
            } else {
                newUrl = currentUrl; // Stay on English
            }
        }
    } else {
        // Handle HTTP URLs (for server deployment)
        if (currentPath.includes('/es/')) {
            newUrl = currentUrl.replace('/es/', lang === 'en' ? '/' : `/${lang}/`);
        } else if (currentPath.includes('/zh_CN/')) {
            newUrl = currentUrl.replace('/zh_CN/', lang === 'en' ? '/' : `/${lang}/`);
        } else {
            if (lang === 'en') {
                newUrl = currentUrl;
            } else {
                const baseUrl = currentUrl.split('/').slice(0, 3).join('/');
                const pathPart = currentUrl.split('/').slice(3).join('/');
                newUrl = `${baseUrl}/${lang}/${pathPart}`;
            }
        }
    }
    
    console.log('Switching from:', currentUrl);
    console.log('Switching to:', newUrl);
    window.location.href = newUrl;
}

function updateLanguageButton() {
    const currentPath = window.location.pathname;
    const currentUrl = window.location.href;
    const langBtn = document.getElementById('langBtn');
    
    if (!langBtn) return;
    
    console.log('Current URL:', currentUrl);
    console.log('Current path:', currentPath);
    
    if (currentPath.includes('/es/') || currentUrl.includes('/es/')) {
        langBtn.innerHTML = '<i class="fas fa-globe"></i> Español';
        console.log('Detected Spanish version');
    } else if (currentPath.includes('/zh_CN/') || currentUrl.includes('/zh_CN/')) {
        langBtn.innerHTML = '<i class="fas fa-globe"></i> 中文';
        console.log('Detected Chinese version');
    } else {
        langBtn.innerHTML = '<i class="fas fa-globe"></i> English';
        console.log('Detected English version');
    }
}
