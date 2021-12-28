import PageAbout from "pages/PageAbout";
import PageCounter from "pages/PageCounter";
import PageLotto from "pages/pageLotto";
import PageYoutube from "pages/pageYoutube";
import TopNav from "components/TopNav";
import { useState } from "react";

function App() {
  const [pageName, setPageName] = useState("about");


  return (
    <div>
    <h1>JinA's React</h1>
    <TopNav changePageName={setPageName}/>
    {pageName === "about" && <PageAbout />}
    {pageName === "counter" && <PageCounter />}
    {pageName === "lotto" && <PageLotto />}
    {pageName === "youtube" && <PageYoutube />}
    </div>
  );
}

export default App;