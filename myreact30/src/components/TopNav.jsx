import './TopNav.css';
import { Menu, Layout } from 'antd';

function TopNav({ changePageName }) {
  const { Header } = Layout;
  return (
    <>
      <Menu mode="horizontal" defaultSelectedKeys={['1']}>
        <Menu.Item key="0" disabled>
          <h1>가나다의 리액트</h1>
        </Menu.Item>
        <Menu.Item key="1" onClick={() => changePageName('about')}>
          About
        </Menu.Item>
        <Menu.Item key="2" onClick={() => changePageName('counter')}>
          카운터
        </Menu.Item>
        <Menu.Item key="3" onClick={() => changePageName('lotto')}>
          로또
        </Menu.Item>
        <Menu.Item key="4" onClick={() => changePageName('playlist')}>
          플레이리스트
        </Menu.Item>
      </Menu>
    </>
  );
}

export default TopNav;
