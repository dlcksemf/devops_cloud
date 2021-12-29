import { useEffect, useState } from 'react';
import Axios from 'axios';

function PageProfile() {
  const [profileList, setProfileList] = useState([]);

  useEffect(
    () =>
      Axios.get(
        'https://classdevopscloud.blob.core.windows.net/data/profile-list.json',
      )
        .then((response) => {
          setProfileList(response.data);
        })
        .catch((error) => console.error(error)),
    [],
  );

  return (
    <div>
      <h2>Page Profile</h2>
      {profileList.length === 0 && <h3>등록된 프로필이 없습니다.</h3>}

      {profileList.map((member) => {
        return (
          <>
            <h3>{member.name}</h3>

            <img src={member.profile_image_url} alt="" />

            <ul>
              <li>{member.role}</li>
              <li>{member.mbti}</li>
              <li>{member.instagram_url}</li>
            </ul>
          </>
        );
      })}
    </div>
  );
}

export default PageProfile;
