import './ProfileList.css';
import ProfileCard from './ProfileCard';

function ProfileList({ profileList }) {
  return (
    <div className="profile-list">
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
