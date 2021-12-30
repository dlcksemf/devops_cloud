import './ProfileCard.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faInstagram } from '@fortawesome/free-brands-svg-icons';
import { faBars, faStickyNote } from '@fortawesome/free-solid-svg-icons';

function ProfileCard({ memberData, className }) {
  const { name, role, mbti, profileImageUrl, instagramUrl } = memberData;

  return (
    <div className="profile-card">
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
          <div className={`image-cropper ${className}`}>
            <img src={profileImageUrl} alt="프로필 이미지" />
          </div>

          <h1>{name}</h1>
          <h2>{role}</h2>
          <h2>{mbti}</h2>

          <a href="#" className={`btnView ${className}`}>
            VIEW MORE
          </a>
          <ul className="contact">
            <li>
              <FontAwesomeIcon icon={faInstagram} />
              <span>
                <a href={instagramUrl} target={'_blank'}>
                  Visit My Instagram page.
                </a>
              </span>
            </li>
          </ul>
        </article>
      </section>
    </div>
  );
}

export default ProfileCard;
