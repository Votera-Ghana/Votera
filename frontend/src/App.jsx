import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Elections from "./pages/Elections";
import ElectionDetails from "./pages/ElectionDetails";
import CandidateDetails from "./pages/CandidateDetails";

import Layout from "./components/Layout/Layout";

function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />

          <Route path="/elections" element={<Elections />} />

          <Route
            path="/elections/:electionId"
            element={<ElectionDetails />}
          />

          <Route
            path="/elections/:electionId/candidate/:candidateId"
            element={<CandidateDetails />}
          />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}

export default App;