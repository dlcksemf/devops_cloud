import "./App.css";
import PageLotto from "./pages/PageLotto";
import ProfileCard from "./components/ProfileCard";
import { useState } from "react";
import userList from "./data/userInfo.json";

function App() {
  const [userNum, setUserNum] = useState("user1");

  return (
    <>
      {userList.map((user) => {
        if (userNum === user.user) {
          return (
            <ProfileCard
              name={user.name}
              role={user.role}
              email={user.email}
              facebook_url={user.facebook_url}
              changeUserPage={setUserNum}
            />
          );
        }
      })}
      <PageLotto />
    </>
  );
}

export default App;
