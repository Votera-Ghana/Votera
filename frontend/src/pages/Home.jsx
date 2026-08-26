import Navbar from "../components/Navbar/Navbar";
import Hero from "../components/Hero/Hero";
import HowItWorks from "../components/HowItWorks/HowItWorks";
import TrustSection from "../components/TrustSection/TrustSection";
import Footer from "../components/Footer/Footer";

function Home() {
  return (
    <>
      <Navbar />
      <Hero />
      <HowItWorks />
      <TrustSection />
      <Footer />
    </>
  );
}

export default Home;