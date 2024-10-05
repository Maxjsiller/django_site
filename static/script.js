document.addEventListener("DOMContentLoaded", function() {
    var consentBanner = document.getElementById('cookie-consent-banner');
    var acceptCookiesButton = document.getElementById('accept-cookies');
    
    if (!localStorage.getItem('cookiesAccepted')) {
      consentBanner.style.display = 'block';
    }
    
    acceptCookiesButton.addEventListener('click', function() {
      localStorage.setItem('cookiesAccepted', 'true');
      consentBanner.style.display = 'none';
    });
  });