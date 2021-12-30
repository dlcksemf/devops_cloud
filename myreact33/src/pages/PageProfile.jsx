import { useEffect, useState } from 'react';
import Axios from 'axios';
import './PageProfile.css';
import ProfileList from 'components/ProfileList';

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
    handleRefresh();
  }, []);

  useEffect(() => {
    setProfileList(profileData);
  }, [profileData]);

  const handleKeyChange = (e) => {
    const value = e.target.value;
    setQuery(value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      setProfileList(
        query
          ? profileData.filter(({ name, role, mbti }) => {
              const pattern = new RegExp(query, 'i');
              const queryTarget = [name, role, mbti];
              return pattern.test(queryTarget);
            })
          : profileData,
      );
    }
  };

  return (
    <div className="page-profile">
      {checkedError && `Error Message: ${checkedError.message}`}

      {profileList.length === 0 && !checkedError && (
        <h3>등록된 프로필이 없습니다.</h3>
      )}

      <hr />

      <button onClick={() => setProfileList([])}>Clear</button>
      <button onClick={handleRefresh}>Refresh</button>
      <div>
        <input
          type="text"
          placeholder="검색어를 입력해주세요!"
          onChange={handleKeyChange}
          onKeyPress={handleKeyPress}
        />
      </div>
      <ProfileList profileList={profileList} />
    </div>
  );
}

export default PageProfile;
