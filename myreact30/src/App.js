import { useState } from 'react';
import PageAbout from 'pages/PageAbout';
import PageCounter from 'pages/PageCounter';
import TopNav from 'components/TopNav';
import PageLotto from 'pages/PageLotto';
import Playlist from 'components/Playlist';

function App() {
  const [pageName, setPageName] = useState('about');

  // const changePageName = (pageName) => {
  //   setPageName(pageName);
  // };

  return (
    <>
      <TopNav changePageName={setPageName} />
      {pageName === 'about' && <PageAbout />}
      {pageName === 'counter' && <PageCounter />}
      {pageName === 'lotto' && <PageLotto />}
      {pageName === 'playlist' && <Playlist />}
    </>
  );
}

export default App;
