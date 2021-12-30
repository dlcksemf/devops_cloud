import "./ProfileCard.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faInstagram } from "@fortawesome/free-brands-svg-icons";
import { faBars, faStickyNote } from "@fortawesome/free-solid-svg-icons";

function ProfileCard({
  name,
  role,
  mbti,
  instagram_url,
  profile_image_url,
  className,
  profileList,
  setSelectedUserId,
  selectedUserId,
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
          <div className="image-cropper">
            <img src={profile_image_url} alt="프로필 이미지" />
          </div>

          <h1>{name}</h1>
          <h2>{role}</h2>
          <h2>{mbti}</h2>

          <a href="#" className="btnView">
            VIEW MORE
          </a>
          <ul className="contact">
            <li>
              <FontAwesomeIcon icon={faInstagram} />
              <span>
                <a href={instagram_url} target={"_blank"}>
                  Visit My Instagram page.
                </a>
              </span>
            </li>
          </ul>
        </article>
        <nav className="others">
          {profileList.map(({ unique_id }, index) => {
            return (
              <a
                onClick={() => setSelectedUserId(unique_id)}
                className={`user${(index % 4) + 1} ${
                  selectedUserId === unique_id ? "on" : ""
                }`}
              ></a>
            );
          })}
        </nav>
      </section>
    </div>
  );
}

export default ProfileCard;
