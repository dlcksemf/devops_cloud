import "./App.css";
import PageLotto from "./pages/PageLotto";
import ProfileCard from "./components/ProfileCard";
import { useState } from "react";
import userList from "./data/userInfo.json";

function App() {
  const [userId, setUserId] = useState("user1");

  return (
    <>
      {userList.map((user, index) => {
        const className = `user${(index % 4) + 1}`;
        if (userId === user.userid) {
          return (
            <ProfileCard
              {...user}
              className={className}
              changeUserPage={setUserId}
            />
          );
        }
      })}
      <PageLotto />
    </>
  );
}

export default App;
