import styled from 'styled-components';

type PlayerContainerProps = {
	spaceBetween: boolean;
};

export const GamePlayContainer = styled.div`
	position: relative;
	display: flex;
	flex-direction: column;
	gap: 2rem;

	@media (min-width: 720px) {
		flex-direction: column-reverse;
	}
`;

export const PlayerContainer = styled.div<PlayerContainerProps>`
	width: 100%;
	display: flex;
	justify-content: ${({ spaceBetween }) => (spaceBetween ? 'space-between' : 'space-around')};
	align-items: center;
`;

export const PlayerIdentity = styled.div`
	width: 100%;
	display: flex;
	justify-content: space-between;
	padding-inline-start: 1.6rem;

	@media (min-width: 720px) {
		padding-inline-start: 2.2rem;
	}

	p {
		font-size: 0.85rem;
		color: white;
		font-weight: 700;
		text-align: center;
		text-transform: uppercase;
		letter-spacing: 2px;
	}
`;

type SecondPlayerProps = {
	large: boolean;
};

export const SecondPlayer = styled.div<SecondPlayerProps>`
	height: 6rem;
	width: 6rem;
	outline: 3px solid transparent;
	border: none;
	border-radius: 50%;
	background-color: hsl(220, 50%, 15%);

	@media (min-width: 720px) {
		width: ${({ large }) => large && `8rem`};
		height: ${({ large }) => large && `8rem`};
	}
`;
