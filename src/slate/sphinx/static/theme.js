(function () {
  var storageKey = "slate-docs-theme";

  function currentTheme() {
    return document.documentElement.dataset.theme === "dark" ? "dark" : "light";
  }

  function applyTheme(theme) {
    document.documentElement.dataset.theme = theme;
    updateThemeButton(theme);
  }

  function updateThemeButton(theme) {
    var label = document.querySelector("[data-theme-label]");
    if (label) {
      label.textContent = theme === "dark" ? "Light mode" : "Dark mode";
    }
  }

  function toggleTheme() {
    var nextTheme = currentTheme() === "dark" ? "light" : "dark";
    try {
      localStorage.setItem(storageKey, nextTheme);
    } catch (error) {
      // Ignore storage failures; the current session still updates.
    }
    applyTheme(nextTheme);
  }

  function setNavOpen(open) {
    document.body.classList.toggle("slate-nav-open", open);
    var toggle = document.querySelector("[data-nav-toggle]");
    if (toggle) {
      toggle.setAttribute("aria-expanded", String(open));
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    updateThemeButton(currentTheme());

    var themeToggle = document.querySelector("[data-theme-toggle]");
    if (themeToggle) {
      themeToggle.addEventListener("click", toggleTheme);
    }

    var navToggle = document.querySelector("[data-nav-toggle]");
    if (navToggle) {
      navToggle.addEventListener("click", function () {
        setNavOpen(!document.body.classList.contains("slate-nav-open"));
      });
    }

    var overlay = document.querySelector("[data-nav-overlay]");
    if (overlay) {
      overlay.addEventListener("click", function () {
        setNavOpen(false);
      });
    }

    document.querySelectorAll(".slate-nav a").forEach(function (link) {
      link.addEventListener("click", function () {
        setNavOpen(false);
      });
    });
  });
})();