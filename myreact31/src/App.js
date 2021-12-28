import "./App.css";
import PageLotto from "./pages/PageLotto";
import ProfileCard from "./components/ProfileCard";
import { useState } from "react";
import userList from "./data/userInfo.json";

function App() {
  const [userNum, setUserNum] = useState("user1");

  return (
    <>
      {userList
        .filter(({ user }) => userNum === user)
        .map((user) => {
          return <ProfileCard {...user} changeUserPage={setUserNum} />;
        })}
      <PageLotto />
    </>
  );
}

export default App;
