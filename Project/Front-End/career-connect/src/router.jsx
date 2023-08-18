import { createBrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import HomePage from "./components/Homepage.jsx";
import ProfilePage from "./components/ProfilePage.jsx";
import SignIn from "./components/SignInPage.jsx";
import Companies from "./components/CompaniesPage.jsx";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            {
                index: true,
                element: <HomePage />,
            },
            {
                path: "ProfilePage",
                element: <ProfilePage />,
            },
            {
                path: "sign-in",
                element: <SignIn/>,
            },
            {
                path: "companies",
                element: <Companies/>,
            },
        ],
    },
]);
export default router;