import './ProfileList.css';
import ProfileCard from './ProfileCard';

function ProfileList({ profileList }) {
  return (
    <div className="profile-list">
      {profileList.length === 0 && <h3>등록된 프로필이 없습니다.</h3>}

      {profileList.map((memberData, index) => {
        const className = `user${(index % 4) + 1}`;
        return (
          <ProfileCard
            memberData={memberData}
            className={className}
            key={memberData.unique_id}
          />
        );
      })}
    </div>
  );
}

export default ProfileList;
