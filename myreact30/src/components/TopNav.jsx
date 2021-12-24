import './TopNav.css';

function TopNav({ changePageName }) {
  return (
    <ul className="top-nav">
      <li>
        <a onClick={() => changePageName('about')}>About</a>
      </li>
      <li>
        <a onClick={() => changePageName('counter')}>카운터</a>
      </li>
      <li>
        <a onClick={() => changePageName('lotto')}>로또</a>
      </li>
      <li>
        <a onClick={() => changePageName('playlist')}>플레이리스트</a>
      </li>
    </ul>
  );
}

export default TopNav;
