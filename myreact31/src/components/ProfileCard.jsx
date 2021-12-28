import "./ProfileCard.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFacebook } from "@fortawesome/free-brands-svg-icons";
import {
  faBars,
  faEnvelope,
  faStickyNote,
} from "@fortawesome/free-solid-svg-icons";

function ProfileCard({
  userid,
  name,
  role,
  email,
  facebook_url,
  children,
  className,
}) {
  return (
    <div className={className}>
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
          <img src={`/profile-images/${userid}.jpg`} alt="프로필 이미지" />

          <h1>{name}</h1>
          <h2>{role}</h2>

          <a href="#" className="btnView">
            VIEW MORE
          </a>
          <ul className="contact">
            <li>
              <FontAwesomeIcon icon={faFacebook} />
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
        <nav className="others">{children}</nav>
      </section>
    </div>
  );
}

export default ProfileCard;
