import ReactPlayer from 'react-player';
import React, { useState } from 'react';
import videoList from 'data/song_list_v2.json';
import { Row, Col } from 'antd';

function Playlist() {
  const [videoUrl, setVideoUrl] = useState();

  return (
    <>
      <Row>
        <Col span={14}>
          {!videoUrl && <div>"영상을 선택 해주세요!"</div>}
          {videoUrl && <ReactPlayer url={videoUrl} />}
        </Col>
        <Col span={10}>
          {videoList.map((video) => {
            return (
              <div
                onClick={() => {
                  setVideoUrl(video.url);
                }}
              >
                <h4>{video.title}</h4>
                <img src={video.thumbnail_url} />
              </div>
            );
          })}
        </Col>
      </Row>
    </>
  );
}

export default Playlist;
