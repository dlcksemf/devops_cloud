import "./App.css";
import PageLotto from "./pages/PageLotto";
import ProfileCard from "./components/ProfileCard";
import { useState, useEffect } from "react";
import Axios from "axios";

function App() {
  const [profileList, setProfileList] = useState([]);
  const [selectedUserId, setSelectedUserId] = useState("bts-jin");

  // App 컴포넌트가 마운트될 때
  // 아래의 함수가 자동 호출 됩니다.
  useEffect(() => {
    Axios.get(
      "https://classdevopscloud.blob.core.windows.net/data/profile-list.json"
    )
      .then((response) => {
        // reponse는 axios 객체
        // response.data => 응답 내용
        setProfileList(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <>
      {profileList.map((user, index) => {
        const className = profileList[index % 4].unique_id;

        if (selectedUserId === user.unique_id) {
          return (
            <ProfileCard {...user} className={className}>
              {profileList.map(({ unique_id }) => {
                return (
                  <a
                    onClick={() => setSelectedUserId(unique_id)}
                    className={selectedUserId === unique_id ? "on" : ""}
                  ></a>
                );
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
