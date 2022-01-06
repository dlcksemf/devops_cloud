import Stars from './Stars';

function Review({ review, type, onClick }) {
  return (
    <div>
      <div
        className="border-2 border-green-400 m-1 p-1 hover:bg-green-200"
        onClick={onClick}
      >
        {review.review.split('\n').map((line) => (
          <>
            {line}
            <br />
          </>
        ))}
        <Stars rating={review.star} type={type} />
      </div>
    </div>
  );
}

export default Review;
