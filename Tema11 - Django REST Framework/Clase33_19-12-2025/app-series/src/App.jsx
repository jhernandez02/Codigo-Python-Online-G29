import { BrowserRouter, Routes, Route } from "react-router-dom";
import CabeceraComponent from "./components/CabeceraComponent";
import PrincipalPage from "./pages/PrincipalPage";
import SeriePage from "./pages/SeriePage";

function App() {
  return (
    <BrowserRouter>
      <CabeceraComponent />
      <Routes>
        <Route path="/" element={<h1 className="mt-3 text-center">Pagina Inicio</h1>} />
        <Route path="/principal" element={<PrincipalPage />} />
        <Route path="/serie/:id" element={<SeriePage />} />
        <Route path="*" element={<h4 className="mt-3 text-center">Error 404 - Página no encontrada</h4>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
