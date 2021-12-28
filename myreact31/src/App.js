import "./App.css";
import PageLotto from "./pages/PageLotto";
import ProfileCard from "./components/ProfileCard";
import { useState } from "react";
import userList from "./data/userInfo.json";

const userIdList = userList.map(({ userid }) => userid);

function App() {
  const [userId, setUserId] = useState(userIdList[0]);

  return (
    <>
      {userList.map((user, index) => {
        const className = userIdList[index % 4];
        if (userId === user.userid) {
          return (
            <ProfileCard {...user} className={className}>
              {userIdList.map((id) => {
                return <a onClick={() => setUserId(id)}></a>;
              })}
            </ProfileCard>
          );
        }
      })}
      <PageLotto />
    </>
  );
}

export default App;
