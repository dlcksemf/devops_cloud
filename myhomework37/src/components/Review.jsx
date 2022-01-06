import { useState } from 'react';
import Stars from './Stars';

function Review({ review, type, handleDelete, handleEdit }) {
  const [showMenu, setShowMenu] = useState(false);

  const handleClickedDeleteButton = () => {
    if (!handleDelete) {
      console.warn('[Review] handleDelete 속성값이 지정되지 않았습니다.');
    } else handleDelete();
  };

  const handleClickedEditButton = () => {
    if (!handleEdit) {
      console.warn('[Review] handleChange 속성값이 지정되지 않았습니다.');
    } else handleEdit();
  };

  return (
    <div>
      <div
        className="relative border-2 border-green-400 m-1 p-1 pt-3"
        onMouseEnter={() => setShowMenu(true)}
        onMouseLeave={() => setShowMenu(false)}
      >
        {showMenu && (
          <div className="text-xs absolute top-0 right-1">
            <span
              className="text-green-900 hover:bg-green-300 cursor-pointer mr-1"
              onClick={handleClickedEditButton}
            >
              수정
            </span>
            <span
              className="text-red-700 hover:bg-red-300 cursor-pointer"
              onClick={handleClickedDeleteButton}
            >
              삭제
            </span>
          </div>
        )}

        {review.review.split('\n').map((line) => (
          <div key={line}>
            {line}
            <br />
          </div>
        ))}
        <Stars rating={review.star} type={type} />
      </div>
    </div>
  );
}

export default Review;
