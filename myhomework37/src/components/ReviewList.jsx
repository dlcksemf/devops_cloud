import Review from './Review.jsx';
import ReviewForm from './ReviewForm.jsx';
import { useState } from 'react';
import useFieldValues from 'hooks/useFieldValues.js';

const INITIAL_STATE = [
  {
    review: '스파이더맨 1 부터 본 사람이면 재미없을 수가 없다',
    star: 5,
  },
  {
    review:
      '전 스파이더맨 두명이 자책했던 일들이 여기서 어느정도 구원받았다는거에 감사드립니다',
    star: 4,
  },
  {
    review:
      '엔드게임을 뛰어넘는 영화가 죽기전에 나올까 생각했었는데.. 2년만에 나왔습니다',
    star: 5,
  },
];

const INITIAL_VALUE = {
  review: '',
  star: 0,
};

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);
  const [showForm, setShowForm] = useState(false);
  const [fieldValues, handleChange, emptyFieldValues] =
    useFieldValues(INITIAL_VALUE);

  const appendReview = () => {
    setReviewList((prevReviewList) => [...prevReviewList, { ...fieldValues }]);
    setShowForm((prevState) => !prevState);
    emptyFieldValues();
  };

  return (
    <div className="w-[400px] m-auto">
      <h2 className="text-xl border-b-2 border-orange-400">Review List</h2>

      {showForm && (
        <ReviewForm handleSubmit={appendReview} handleChange={handleChange} />
      )}
      {!showForm && (
        <button
          className="text-sm bg-orange-200 hover:bg-orange-300 border rounded-md my-2 p-1"
          onClick={() => setShowForm((prevState) => !prevState)}
        >
          New Review
        </button>
      )}

      {reviewList.map((review) => (
        <Review review={review} />
      ))}
    </div>
  );
}

export default ReviewList;
