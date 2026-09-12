(() => {
  const storageKey = "arielle-theme";
  const root = document.documentElement;
  const systemTheme = window.matchMedia("(prefers-color-scheme: dark)");
  let preference = null;
  let storageAvailable = true;

  function validTheme(value) {
    return value === "light" || value === "dark";
  }

  function readPreference() {
    try {
      const saved = localStorage.getItem(storageKey);
      return validTheme(saved) ? saved : null;
    } catch {
      storageAvailable = false;
      return undefined;
    }
  }

  const savedPreference = readPreference();
  const linkedPreference = new URL(window.location.href).searchParams.get("theme");
  preference = savedPreference || (validTheme(linkedPreference) ? linkedPreference : null);

  function updatePageLinks() {
    // Carry the choice in links if storage is blocked or files are opened locally.
    if (storageAvailable && window.location.protocol !== "file:") return;
    document.querySelectorAll('.navigation a, .profile a[href^="."]').forEach((link) => {
      const url = new URL(link.href);
      url.searchParams.set("theme", root.dataset.theme);
      link.href = url.href;
    });
  }

  function applyTheme(theme) {
    root.dataset.theme = theme;
    const button = document.querySelector(".theme-toggle");
    if (button) {
      const label = `Switch to ${theme === "dark" ? "light" : "dark"} theme`;
      button.setAttribute("aria-label", label);
      button.title = label;
    }
    updatePageLinks();
  }

  function synchronizeTheme() {
    const saved = readPreference();
    if (saved !== undefined) preference = saved;
    applyTheme(preference || (systemTheme.matches ? "dark" : "light"));
  }

  // Set the palette before the page is painted to avoid a light flash.
  applyTheme(preference || (systemTheme.matches ? "dark" : "light"));

  // Back/Forward can restore a page without rerunning this script.
  window.addEventListener("pageshow", (event) => {
    if (event.persisted) synchronizeTheme();
  });
  window.addEventListener("storage", (event) => {
    if (event.key === storageKey || event.key === null) synchronizeTheme();
  });

  function followSystemTheme(event) {
    if (!preference) applyTheme(event.matches ? "dark" : "light");
  }

  if (typeof systemTheme.addEventListener === "function") {
    systemTheme.addEventListener("change", followSystemTheme);
  } else if (typeof systemTheme.addListener === "function") {
    // Older Safari versions expose the legacy MediaQueryList API.
    systemTheme.addListener(followSystemTheme);
  }

  function initializeToggle() {
    const button = document.querySelector(".theme-toggle");
    if (!button) return;
    applyTheme(root.dataset.theme);
    button.hidden = false;
    button.addEventListener("click", () => {
      preference = root.dataset.theme === "dark" ? "light" : "dark";
      applyTheme(preference);
      try {
        localStorage.setItem(storageKey, preference);
      } catch {
        storageAvailable = false;
      }
      updatePageLinks();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeToggle, { once: true });
  } else {
    initializeToggle();
  }
})();
