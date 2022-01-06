import Stars from './Stars';

function Review({ review }) {
  return (
    <div>
      <div className="border-2 border-green-400 m-1 p-1 hover:bg-green-200">
        {review.review.split('\n').map((line) => (
          <>
            {line}
            <br />
          </>
        ))}
        <Stars rating={review.star} />
      </div>
    </div>
  );
}

export default Review;
