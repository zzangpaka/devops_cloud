import PageLotto from "./PageLotto";
import ProfileCard from "./ProfileCard";
import Profile from "./data/profile.json";
import profileImage1 from "./img/member1.jpg";
import profileImage2 from "./img/member2.jpg";
import profileImage3 from "./img/member3.jpg";
import profileImage4 from "./img/member4.jpg";
import { useState } from "react";
import TopNav from "./TopNav";



function App() {
  const [Page, setPage] = useState("Member1");
	return (
		<div>
      <TopNav changePage={setPage} />
      {Page === "Lotto" && <PageLotto />}
      
      {Page === "Member1" && (
        <ProfileCard
          changePage={setPage}
          profileImage={profileImage1}
          name={"DCODELAB"}
          role={"UI/UX INTERACTIVE DEVELOPER"}
          facebook_url={"Visit My Facebook page"}
          email={"hadaboni80@naver.com"} />)}

      {Page === "Member2" && (
        <ProfileCard
          changePage={setPage}
          profileImage={profileImage2}
          name={"DCODELAB"}
          role={"UI/UX INTERACTIVE DEVELOPER"}
          facebook_url={"Visit My Facebook page"}
          email={"hadaboni80@naver.com"} />)}

      {Page === "Member3" && (
        <ProfileCard
          changePage={setPage}
          profileImage={profileImage3}
          name={"DCODELAB"}
          role={"UI/UX INTERACTIVE DEVELOPER"}
          facebook_url={"Visit My Facebook page"}
          email={"hadaboni80@naver.com"} />)}

			{Page === "Member4" && (
        <ProfileCard
          changePage={setPage}
          profileImage={profileImage4}
          name={"DCODELAB"}
          role={"UI/UX INTERACTIVE DEVELOPER"}
          facebook_url={"Visit My Facebook page"}
          email={"hadaboni80@naver.com"} />)}
		</div>
	)
}

export default App;
