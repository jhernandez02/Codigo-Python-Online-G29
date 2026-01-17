import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AppProvider } from "./contexts/AppContext";
import CabeceraComponent from "./components/CabeceraComponent";
import PrincipalPage from "./pages/PrincipalPage";
import MembresiaPage from "./pages/MembresiaPage";
import HistorialPage from "./pages/HistorialPage";
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <AppProvider>
        <CabeceraComponent />
        <Routes>
          <Route path="/" element={<PrincipalPage />} />
          <Route path="/membresias" element={<MembresiaPage />} />
          <Route path="/historial" element={<HistorialPage />} />
          <Route path="*" element={<h4 className="mt-3 text-center">Error 404 - Página no encontrada</h4>} />
        </Routes>
      </AppProvider>
    </BrowserRouter>
  );
}

export default App;
