import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Elections from "./pages/Elections";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/elections" element={<Elections />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;