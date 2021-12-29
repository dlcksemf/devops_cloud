import { useEffect, useState } from 'react';
import Axios from 'axios';

function PageProfile() {
  const [profileData, setProfileData] = useState([]);
  const [checkedError, setCheckedError] = useState(null);
  const [query, setQuery] = useState(null);
  const [profileList, setProfileList] = useState([]);

  const handleRefresh = () => {
    setCheckedError(null);
    Axios.get(
      'https://classdevopscloud.blob.core.windows.net/data/profile-list.json',
    )
      .then((response) => {
        const profileList = response.data.map((profile) => ({
          ...profile,
          profileImageUrl: profile.profile_image_url,
          instagramUrl: profile.instagram_url,
        }));
        setProfileData(profileList);
      })
      .catch((error) => {
        setCheckedError(error);
      });
  };

  useEffect(() => {
    profileData.length === 0 && handleRefresh();
    setProfileList(profileData);
  }, [profileData]);

  const handleKeyChange = (e) => {
    const value = e.target.value;
    setQuery(value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      query &&
        setProfileList(
          profileData.filter((profile) =>
            Object.values(profile).some((info) => info.includes(query)),
          ),
        );
    }
  };

  return (
    <div>
      <h2>Page Profile</h2>

      {checkedError && `Error Message: ${checkedError.message}`}

      <hr />

      <button onClick={() => setProfileList([])}>Clear</button>
      <button onClick={handleRefresh}>Refresh</button>

      <hr />
      <input
        type="text"
        placeholder="검색어를 입력해주세요!"
        onChange={handleKeyChange}
        onKeyPress={handleKeyPress}
      />

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
