import ReactPlayer from 'react-player';
import React, { useState } from 'react';
import videoList from 'data/song_list_v2.json';
import { Layout, List, Avatar } from 'antd';

function Playlist() {
  const [videoUrl, setVideoUrl] = useState();
  const { Content, Footer, Sider } = Layout;

  return (
    <>
      <Layout>
        <Layout className="site-layout" style={{ marginLeft: 200 }}>
          <Content style={{ margin: '24px 16px 0', overflow: 'initial' }}>
            <div
              className="site-layout-background"
              style={{ padding: 24, textAlign: 'center' }}
            >
              {!videoUrl && <div>"영상을 선택 해주세요!"</div>}
              {videoUrl && <ReactPlayer url={videoUrl} />}
            </div>
          </Content>

          <Sider
            style={{
              overflow: 'auto',
              height: '100vh',
              position: 'fixed',
              right: 0,
              padding: 24,
            }}
            theme="light"
            width={400}
          >
            <List
              itemLayout="horizontal"
              dataSource={videoList}
              renderItem={(item) => (
                <List.Item onClick={() => setVideoUrl(item.url)}>
                  <List.Item.Meta
                    avatar={<Avatar src={item.thumbnail_url} />}
                    title={<h5>{item.title}</h5>}
                  />
                </List.Item>
              )}
            />
          </Sider>
        </Layout>
        <Footer style={{ textAlign: 'center' }}>2021.12.24</Footer>
      </Layout>
    </>
  );
}

export default Playlist;
