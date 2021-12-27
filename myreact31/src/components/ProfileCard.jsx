import "./ProfileCard.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFacebook } from "@fortawesome/free-brands-svg-icons";
import {
  faBars,
  faEnvelope,
  faStickyNote,
} from "@fortawesome/free-solid-svg-icons";
import profileImage from "../image/member1.jpg";

function ProfileCard({ name, role, email, facebook_url, changeUserPage }) {
  return (
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
        <ul className="contact">
          <li>
            <FontAwesomeIcon className="icon" icon={faFacebook} />{" "}
            <span>
              <a href={facebook_url} target={"_blank"}>
                Visit My Facebook page.
              </a>
            </span>
          </li>
          <li>
            <FontAwesomeIcon icon={faEnvelope} />
            <span>{email}</span>
          </li>
        </ul>
      </article>
      <nav className="others">
        <a onClick={() => changeUserPage("user1")}></a>
        <a onClick={() => changeUserPage("user2")}></a>
        <a onClick={() => changeUserPage("user3")}></a>
        <a onClick={() => changeUserPage("user4")}></a>
      </nav>
    </section>
  );
}

export default ProfileCard;
