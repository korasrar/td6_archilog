import { defineStore } from "pinia";
import { ref } from "vue";

export const useAuthStore = defineStore("auth", () => {
  const HARDCODED_PASSWORD = "admin123";

  const isAuthenticated = ref(false);

  const login = (password) => {
    if (password === HARDCODED_PASSWORD) {
      isAuthenticated.value = true;
      localStorage.setItem("isAuthenticated", "true");
      return true;
    }
    return false;
  };

  const logout = () => {
    isAuthenticated.value = false;
    localStorage.removeItem("isAuthenticated");
  };

  const initAuth = () => {
    const savedAuth = localStorage.getItem("isAuthenticated");
    if (savedAuth === "true") {
      isAuthenticated.value = true;
    }
  };

  return {
    isAuthenticated,
    login,
    logout,
    initAuth,
  };
});
