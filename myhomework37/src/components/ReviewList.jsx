import Review from './Review.jsx';
import ReviewForm from './ReviewForm.jsx';
import { useState } from 'react';
import useFieldValues from 'hooks/useFieldValues.js';
import './ReviewList.css';

const INITIAL_STATE = [
  {
    id: 1,
    review: '스파이더맨 1 부터 본 사람이면 재미없을 수가 없다',
    star: 5,
  },
  {
    id: 2,
    review:
      '전 스파이더맨 두명이 자책했던 일들이 여기서 어느정도 구원받았다는거에 감사드립니다',
    star: 4,
  },
  {
    id: 3,
    review:
      '엔드게임을 뛰어넘는 영화가 죽기전에 나올까 생각했었는데.. 2년만에 나왔습니다',
    star: 5,
  },
];

const INITIAL_VALUE = {
  review: '',
  star: 0,
};

const ACTION_TYPES = {
  DELETE_REVIEW: 'DELETE_REVIEW',
  CHANGE_REVIEW: 'CHANGE_REVIEW',
};

function reducer(reviewList, action) {
  const { type, reviewIndex } = action;
  switch (type) {
    case ACTION_TYPES.DELETE_REVIEW: {
      return reviewList.filter((_, index) => index !== reviewIndex);
    }
    default:
      return reviewList;
  }
}

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);
  const [showForm, setShowForm] = useState(false);
  const [fieldValues, handleChange, emptyFieldValues] =
    useFieldValues(INITIAL_VALUE);
  const [reviewIconType, setReviewIconType] = useState(false);

  // 새로운 리뷰 저장
  const appendReview = () => {
    // review는 데이터베이스에 저장하면 id를 할당해줍니다.
    // 지금은 random한 숫자 적용
    const reviewId = new Date().getTime();

    const review = { ...fieldValues, id: reviewId };
    setReviewList((prevReviewList) => [...prevReviewList, review]);
    setShowForm((prevState) => !prevState);
    emptyFieldValues();
  };

  const iconChange = () => {
    setReviewIconType((prevState) => !prevState);
  };

  const deleteReview = (index) => {
    const action = { type: ACTION_TYPES.DELETE_REVIEW, reviewIndex: index };
    setReviewList((prevReviewList) => reducer(prevReviewList, action));
  };

  const editReview = (index) => {
    const action = { type: ACTION_TYPES.CHANGE_REVIEW, reviewIndex: index };
  };

  return (
    <div className="w-[400px] m-auto">
      <h2 className="text-xl border-b-2 border-orange-400">Review List</h2>

      {showForm && (
        <ReviewForm handleSubmit={appendReview} handleChange={handleChange} />
      )}
      {!showForm && (
        <div className="grid grid-cols-3 gap-4 content-center">
          <button
            className="text-sm bg-orange-200 hover:bg-orange-300 border rounded-md my-3 py-2 px-3"
            onClick={() => setShowForm((prevState) => !prevState)}
          >
            New Review
          </button>

          <div />

          <div className="mb-6">
            <label
              htmlFor="toggle-example"
              className="flex items-center cursor-pointer relative my-2"
            >
              <input
                type="checkbox"
                id="toggle-example"
                className="sr-only"
                name="star"
                onClick={iconChange}
              />
              <div className="toggle-bg bg-gray-200 border-2 border-gray-200 h-6 w-11 rounded-full"></div>
              <span className="ml-3 text-gray-900 text-sm font-medium">
                Icon
              </span>
            </label>
          </div>
        </div>
      )}

      {reviewList.map((review, index) => (
        <Review
          key={review.id}
          review={review}
          type={reviewIconType}
          handleDelete={() => deleteReview(index)}
          handleEdit={() => editReview(index)}
        />
      ))}
    </div>
  );
}

export default ReviewList;
