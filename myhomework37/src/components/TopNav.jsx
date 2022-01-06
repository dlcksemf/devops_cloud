import { Link } from 'react-router-dom';

function TopNav() {
  return (
    <div className="my-3">
      <ul className="flex gap-4">
        <li>
          <NavLink to="/">Home</NavLink>
        </li>
        <li>
          <NavLink to="about">About</NavLink>
        </li>
        <li>
          <NavLink to="reviews">Review</NavLink>
        </li>
      </ul>
    </div>
  );
}

function NavLink({ to, children }) {
  return (
    <Link
      to={to}
      className="border-red-400 hover:border-b-4 pb-1 hover:text-red-400 duration-75 text-sm"
    >
      {children}
    </Link>
  );
}

export default TopNav;
