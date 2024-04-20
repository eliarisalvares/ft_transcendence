import notFound from "../views/404.js";
import forgotPassword from "../views/auth/forgotPassword.js";
import login from "../views/auth/login.js";
import signup from "../views/auth/signup.js";
import twoFactorAuth from "../views/auth/validate2Factor.js";
import userManagement from "../views/user_management/user_management.js";
import GameInfoView from "../views/game-info/game_info.js";
/**
 * An object representing the routes in the application.
 * Each key is a path, and the value is an object with a title and a render function.
 * @type {Object.<string, {title: string, render: function}>}
 */
const pathRoutes = {
  "/": { title: "Login", render: login, description: "Login to your account."},
  "/login": { title: "Login", render: login, description: "Login to your account."},
  "/404": { title: "Not Found", render: notFound, description: "The page you are looking for does not exist."},
};

const hashRoutes = {
  "/": { title: "User Management", render: userManagement, description: "Manage users.", isProtected: true },
  "login": { title: "Login", render: login, description: "Login to your account."},
  "sign-up": { title: "Signup", render: signup, description: "Create an account." },
  "404": { title: "Not Found", render: notFound, description: "The page you are looking for does not exist."},
  "two-factor-auth": { title: "Two Factor Auth", render: twoFactorAuth, description: "Two Factor Authentication."},
  "forgot-password": { title: "Forgot Password", render: forgotPassword, description: "Forgot Password."},
  "user-management": { title: "User Management", render: userManagement, description: "Manage users."},
  "game-info": { title: "Game info", render: GameInfoView, description: "Game info page."}
};

export {
  hashRoutes,
  pathRoutes
};
