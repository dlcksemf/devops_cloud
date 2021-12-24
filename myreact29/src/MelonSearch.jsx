import { Typography, List, Avatar, Input, Space, notification } from 'antd';
import { useState } from 'react';

import Axios from 'axios';
import jsonpAdapter from 'axios-jsonp';

const { Search } = Input;

function MelonSearch() {
  const [query, setQuery] = useState('');
  const [songList, setSongList] = useState([]);

  const handleChange = (e) => {
    const {
      target: { value },
    } = e;
    console.group('handleChange');
    console.log(value);
    console.groupEnd();
    setQuery(value);
  };

  const handlePressEnter = () => {
    console.group('handlePressEnter');
    console.log(`검색어 ${query}(으)로 검색합니다.`);
    console.groupEnd();

    const url = 'https://www.melon.com/search/keyword/index.json';

    Axios({
      url: url,
      adapter: jsonpAdapter,
      callbackParamName: 'jscallback',
      params: {
        query: query,
      },
    })
      .then((response) => {
        const {
          data: { SONGCONTENTS: searchedSongList = [] },
        } = response;
        console.group('멜론 검색결과');
        console.log(response);
        console.log(searchedSongList);
        console.groupEnd();
        setSongList(searchedSongList);

        const type = 'info';
        notification[type]({
          message: '멜론 검색',
          description: `${searchedSongList.length}개의 노래 검색 결과가 있습니다.`,
        });
      })
      .catch((error) => {
        console.group('멜론 검색 에러');
        console.error(error);
        console.groupEnd();

        notification.error({
          message: '멜론 검색 에러',
          // 주의: 유저 친화적인 에러 메세지는 아닙니다.
          description: JSON.stringify(error),
        });
      });
  };

  return (
    <div style={{ width: 500, margin: '0 auto' }}>
      <h2>멜론 검색</h2>
      <hr />
      <Space direction="vertical">
        <Search
          placeholder="검색어를 입력해주세요."
          onChange={handleChange}
          onSearch={handlePressEnter}
          style={{ width: 200 }}
        />
      </Space>
      <hr />
      검색어 : {query}
      <List
        itemLayout="horizontal"
        dataSource={songList}
        renderItem={(item) => (
          <List.Item>
            <List.Item.Meta
              avatar={<Avatar src={item.ALBUMIMG} />}
              description={item.ARTISTNAME}
            />
            <Typography.Text
              onClick={() => {
                console.log(`clicked ${JSON.stringify(item)}`);
              }}
            >
              <a
                href={`https://www.melon.com/song/detail.htm?songId=${item.SONGID}`}
                target={'_blank'}
              >
                {item.SONGNAME}
              </a>
            </Typography.Text>
          </List.Item>
        )}
      />
      {/* {songList.map((song) => {
        return (
          <div>
            <img src={song.ALBUMIMG} />
            {song.SONGNAME} by {song.ARTISTNAME}
          </div>
        );
      })} */}
    </div>
  );
}

export default MelonSearch;
