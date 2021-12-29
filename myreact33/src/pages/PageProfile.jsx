import { useState } from 'react';

function PageProfile() {
  const [profileList, setProfileList] = useState([
    {
      uniqueId: 'bts-jin',
      name: '진',
      role: '서브보컬',
      mbti: 'INFP',
      instagramUrl: 'https://instagram.com/jin',
      profileImageUrl:
        'https://classdevopscloud.blob.core.windows.net/data/bts-jin.jpg',
    },
  ]);

  return (
    <div>
      <h2>Page Profile</h2>
      {profileList.length === 0 && <h3>등록된 프로필이 없습니다.</h3>}

      {profileList.map((member) => {
        return (
          <>
            <h3>{member.name}</h3>

            <img src={member.profileImageUrl} alt="" />

            <ul>
              <li>{member.role}</li>
              <li>{member.mbti}</li>
              <li>{member.instagramUrl}</li>
            </ul>
          </>
        );
      })}
    </div>
  );
}

export default PageProfile;
