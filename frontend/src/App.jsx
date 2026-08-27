import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Elections from "./pages/Elections";
import ElectionDetails from "./pages/ElectionDetails";
import CandidateDetails from "./pages/CandidateDetails";

import Layout from "./components/Layout/Layout";
import AdminLayout from "./components/AdminLayout/AdminLayout";

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
            ADMIN PANEL
        ========================== */}

        <Route
          path="/admin/election/:electionId"
          element={<AdminLayout />}
        >

          <Route
            index
            element={<div>Admin Overview</div>}
          />

          <Route
            path="election"
            element={<div>Election Management</div>}
          />

          <Route
            path="positions"
            element={<div>Positions Management</div>}
          />

          <Route
            path="candidates"
            element={<div>Candidates Management</div>}
          />

          <Route
            path="voters"
            element={<div>Voters Management</div>}
          />

          <Route
            path="transactions"
            element={<div>Transactions</div>}
          />

          <Route
            path="results"
            element={<div>Election Results</div>}
          />

          <Route
            path="settings"
            element={<div>Election Settings</div>}
          />

        </Route>

      </Routes>

    </BrowserRouter>
  );
}

export default App;