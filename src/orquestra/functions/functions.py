"""Protocols describing different kinds of functions."""
from typing import NamedTuple, Callable, Any, TypeVar
from typing_extensions import Protocol, runtime_checkable
import numpy as np

T = TypeVar("T", covariant=True)
S = TypeVar("S", contravariant=True)


@runtime_checkable
class CallableWithGradient(Protocol):
    def __call__(self, params: np.ndarray):
        pass

    def gradient(self, params: np.ndarray) -> np.ndarray:
        pass


@runtime_checkable
class CallableStoringArtifacts(Protocol[S, T]):
    def __call__(
        self, params: S, store_artifact: Callable[[str, Any, bool], None]
    ) -> T:
        pass


@runtime_checkable
class CallableWithGradientStoringArtifacts(
    CallableStoringArtifacts[np.ndarray, T], Protocol
):
    def gradient(self, params: np.ndarray) -> np.ndarray:
        pass


class FunctionWithGradient(NamedTuple):
    function: Callable[[np.ndarray], np.ndarray]
    gradient: Callable[[np.ndarray], np.ndarray]

    def __call__(self, params: np.ndarray):
        return self.function(params)
