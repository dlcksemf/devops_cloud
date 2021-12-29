import { useEffect, useState } from 'react';
import Axios from 'axios';

function PageProfile() {
  const [profileList, setProfileList] = useState([]);

  useEffect(() => {
    Axios.get(
      'https://classdevopscloud.blob.core.windows.net/data/profile-list.json',
    )
      .then((response) => {
        const profileList = response.data.map((profile) => ({
          ...profile,
          profileImageUrl: profile.profile_image_url,
          instagramUrl: profile.instagram_url,
        }));
        setProfileList(profileList);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h2>Page Profile</h2>

      <button onClick={() => setProfileList([])}>Clear</button>

      {profileList.length === 0 && <h3>등록된 프로필이 없습니다.</h3>}

      {profileList.map((member) => {
        return (
          <div key={member.unique_id}>
            <h3>{member.name}</h3>

            <img src={member.profileImageUrl} alt="" />

            <ul>
              <li>{member.role}</li>
              <li>{member.mbti}</li>
              <li>{member.instagramUrl}</li>
            </ul>
          </div>
        );
      })}
    </div>
  );
}

export default PageProfile;
