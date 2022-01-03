import "./ProfileCard.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faBars,
  faEnvelope,
  faStickyNote,
} from "@fortawesome/free-solid-svg-icons";
import { faFacebook } from "@fortawesome/free-brands-svg-icons";

function ProfileCard({
  changePage,
  profileImage,
  name,
  role,
  facebook_url,
  email,
}) {
  return (
    <div className="Member1">
      <section>
        <nav className="menu">
          <a href="#">
            <FontAwesomeIcon icon={faBars} />
          </a>
          <a href="#">
            <FontAwesomeIcon icon={faStickyNote} />
          </a>
        </nav>
        <article className="profile">
          <img src={profileImage} alt="프로필 이미지" />

          <h1>{name}</h1>
          <h2>{role}</h2>

          <a href="#" className="btnView">
            VIEW MORE
          </a>
        </article>
        <ul className="contact">
          <li>
            <FontAwesomeIcon icon={faFacebook} />
            <span>{facebook_url}</span>
          </li>
          <li>
            <FontAwesomeIcon icon={faEnvelope} />
            <span>{email}</span>
          </li>
        </ul>
        <nav className="others">
          <a onClick={() => changePage("Member1")}></a>
          <a onClick={() => changePage("Member2")}></a>
          <a onClick={() => changePage("Member3")}></a>
          <a onClick={() => changePage("Member4")}></a>
        </nav>
      </section>
    </div>
  );
}

export default ProfileCard;
