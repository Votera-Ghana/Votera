import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Elections from "./pages/Elections";
import ElectionDetails from "./pages/ElectionDetails";
import CandidateDetails from "./pages/CandidateDetails";
import Layout from "./components/Layout/Layout";
import AdminLogin from "./pages/AdminLogin/AdminLogin";
import AdminDashboard from "./pages/Admin/AdminDashboard";
import ElectionManagement from "./pages/Admin/ElectionManagement";
import PositionsManagement from "./pages/Admin/PositionsManagement";
import AdminCandidates from "./pages/AdminCandidates/AdminCandidates";
import AdminVoters from "./pages/AdminVoters/AdminVoters";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        {/* =========================
            PUBLIC WEBSITE
        ========================== */}

        <Route element={<Layout />}>

          <Route
            path="/"
            element={<Home />}
          />

          <Route
            path="/elections"
            element={<Elections />}
          />

          <Route
            path="/elections/:electionId"
            element={<ElectionDetails />}
          />

          <Route
            path="/elections/:electionId/candidate/:candidateId"
            element={<CandidateDetails />}
          />

        </Route>


        {/* =========================
            ADMIN
        ========================== */}

        <Route
          path="/admin/login"
          element={<AdminLogin />}
        />

        <Route
          path="/admin/election/:electionId"
          element={<AdminDashboard />}
        />

        <Route
          path="/admin/election/:electionId/election"
          element={<ElectionManagement />}
        />

        <Route
            path="/admin/election/:electionId/positions"
          element={<PositionsManagement />}
        />

        <Route
          path="/admin/election/:electionId/candidates"
          element={<AdminCandidates />}
        />

        <Route
          path="/admin/election/:electionId/voters"
          element={<AdminVoters />}
        />

        
      </Routes>
    </BrowserRouter>
  );
}

export default App;