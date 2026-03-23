from odrpack import odr_fit
import numpy as np
import pandas as pd
from time import time


def exp_jacobian_beta(x: np.ndarray, beta: np.ndarray) -> np.ndarray:
    """
    Jacobian of the model function.
    Output shape: (q=1, npar, n)
    """
    n = len(x)
    npar = len(beta)

    J = np.empty((n, npar))
    J[:, 0] = np.exp(beta[1] * x)
    J[:, 1] = beta[0] * x * np.exp(beta[1] * x)

    # (n, npar) -> (npar, n) -> (1, npar, n)
    return J.T[np.newaxis, :, :]


def main_pol_5():
    def f(x: np.ndarray, beta: np.ndarray) -> np.ndarray:
        "Model function."
        return (
            beta[0] * x**5
            + beta[1] * x**4
            + beta[2] * x**3
            + beta[3] * x**2
            + beta[4] * x
            + beta[5]
        )

    xdata = np.linspace(-10, 10, 100)
    ydata = f(xdata, np.array([1, 1, 1, 2, 1, 0])) + np.random.randn(len(xdata)) * 100
    df = pd.DataFrame({"x": xdata, "y": ydata})
    print()


def main_pol_2():
    def f(x: np.ndarray, beta: np.ndarray) -> np.ndarray:
        "Model function."
        return beta[0] * x**2 + beta[1] * x + beta[2]

    xdata = np.array([0.982, 1.998, 4.978, 6.01])
    ydata = np.array([2.7, 7.4, 148.0, 403.0])
    sy = np.array(
        [
            0.1,
            0.1,
            0.25,
            0.1,
        ]
    )
    sx = 0.01
    df = pd.DataFrame({"x": xdata, "y": ydata})

    beta0 = np.array([1.0, 1.0, 1.0])
    # bounds = (np.array([0.0, 0.0]), np.array([10.0, 0.9]))
    bounds = None
    fix_beta = np.array([0, 0, 1])  # all parameters free
    sol = odr_fit(
        f,
        xdata,
        ydata,
        beta0,
        weight_y=1 / sy**2 if sy is not None else None,
        weight_x=1 / sx**2 if sx is not None else None,
        bounds=bounds,
        # jac_beta=exp_jacobian_beta,
        # task="OLS",
        task="explicit-ODR",
        fix_beta=fix_beta,
    )

    print("beta:", sol.beta)
    print(f"cov_matrix = \n{sol.cov_beta}")
    print(f"Number of iterations: {sol.niter}")
    print()


def main():
    xdata = np.array([0.982, 1.998, 4.978, 6.01])
    ydata = np.array([2.7, 7.4, 148.0, 403.0])
    sy = np.array(
        [
            0.1,
            0.1,
            0.25,
            0.1,
        ]
    )
    sx = 0.01
    df = pd.DataFrame({"x": xdata, "y": ydata})

    beta0 = np.array([1.0, 1.0])
    # bounds = (np.array([0.0, 0.0]), np.array([10.0, 0.9]))
    bounds = None

    def f(x: np.ndarray, beta: np.ndarray) -> np.ndarray:
        "Model function."
        return beta[0] * np.exp(beta[1] * x)

    sol = odr_fit(
        f,
        xdata,
        ydata,
        beta0,
        weight_y=1 / sy**2 if sy is not None else None,
        weight_x=1 / sx**2 if sx is not None else None,
        bounds=bounds,
        # jac_beta=exp_jacobian_beta,
        # task="OLS",
        task="explicit-ODR",
    )

    print("beta:", sol.beta)
    print(f"cov_matrix = \n{sol.cov_beta}")
    print(f"Number of iterations: {sol.niter}")
    print()


def main_2():
    def f(x: np.ndarray, beta: np.ndarray) -> np.ndarray:
        "Model function."
        return beta[0] * np.exp(beta[1] * x)

    sy = 0.85

    xdata = np.linspace(1, 10, 1500)
    ydata = f(xdata, np.array([2.0, 0.005])) + np.random.randn(len(xdata)) * np.sqrt(sy)
    sy = np.array([sy] * len(xdata))
    df = pd.DataFrame({"x": xdata, "y": ydata})

    beta0 = np.array([1.0, 1.0])
    # bounds = (np.array([0.0, 0.0]), np.array([10.0, 0.9]))
    bounds = None
    t0 = time()
    sol = odr_fit(
        f,
        xdata,
        ydata,
        beta0,
        weight_y=1 / sy**2 if sy is not None else None,
        bounds=bounds,
        jac_beta=exp_jacobian_beta,
        task="OLS",
        sstol=1e-12,
    )
    print(f"Time with jacobian: {time() - t0:.4f} s")

    print(f"Success: {sol.success}")
    print(f"Stop reason: {sol.stopreason}")
    print("beta:", sol.beta)
    print("delta:", sol.delta)
    print(f"Number of iterations: {sol.niter}")
    print(f"Chi squared: {sol.sum_square**2}")
    print()

    print("Without jacobian:")
    t0 = time()
    sol2 = odr_fit(
        f,
        xdata,
        ydata,
        beta0,
        weight_y=1 / sy**2 if sy is not None else None,
        bounds=bounds,
        task="OLS",
        sstol=1e-12,
    )
    print(f"Time without jacobian: {time() - t0:.4f} s")

    print(f"Success: {sol2.success}")
    print(f"Stop reason: {sol2.stopreason}")
    print("beta:", sol2.beta)
    print("delta:", sol2.delta)
    print(f"Number of iterations: {sol2.niter}")
    print(f"Chi squared: {sol2.sum_square**2}")
    print()


def main_3():
    def f(x: np.ndarray, beta: np.ndarray) -> np.ndarray:
        b1, b2 = beta
        return (b1 * x**2 + x * (1 - x)) / (
            b1 * x**2 + 2 * x * (1 - x) + b2 * (1 - x) ** 2
        )

    sy = 0.02
    xdata = np.linspace(0, 1, 50)
    ydata = f(xdata, np.array([0.3, 0.7])) + np.random.randn(len(xdata)) * np.sqrt(sy)
    sy = np.array([sy] * len(xdata))
    df = pd.DataFrame({"x": xdata, "y": ydata})

    def jacobian_beta(x: np.ndarray, beta: np.ndarray) -> np.ndarray:
        n = len(x)
        npar = len(beta)

        J = np.empty((n, npar))
        b1, b2 = beta
        x2 = x**2
        omx = 1 - x  # one minus x
        omx2 = omx**2  # (1-x)^2
        x_omx = x * omx  # x(1-x)

        u = b1 * x2 + x_omx
        v = b1 * x2 + 2 * x_omx + b2 * omx2
        denom_jac = v**2
        diff_v_u = x_omx + b2 * omx2
        J[:, 0] = (x2 * diff_v_u) / denom_jac
        J[:, 1] = -(u * omx2) / denom_jac

        return J.T[np.newaxis, :, :]

    beta0 = np.array([0.5, 0.5])
    # bounds = (np.array([0.0, 0.0]), np.array([1.0, 1.0]))
    t0 = time()
    sol = odr_fit(
        f,
        xdata,
        ydata,
        beta0,
        weight_y=1 / sy**2 if sy is not None else None,
        bounds=None,
        jac_beta=jacobian_beta,
        task="OLS",
        sstol=1e-12,
    )
    print(f"Time with jacobian: {time() - t0:.4f} s")
    print(f"Success: {sol.success}")
    print(f"Stop reason: {sol.stopreason}")
    print("beta:", sol.beta)
    print(f"Number of iterations: {sol.niter}")
    print(f"Chi squared: {sol.sum_square**2}")

    t0 = time()
    sol2 = odr_fit(
        f,
        xdata,
        ydata,
        beta0,
        weight_y=1 / sy**2 if sy is not None else None,
        bounds=None,
        task="OLS",
        sstol=1e-12,
    )
    print(f"Time without jacobian: {time() - t0:.4f} s")
    print(f"Success: {sol2.success}")
    print(f"Stop reason: {sol2.stopreason}")
    print("beta:", sol2.beta)
    print(f"Number of iterations: {sol2.niter}")
    print(f"Chi squared: {sol2.sum_square**2}")


if __name__ == "__main__":
    main_pol_5()
    # main_pol_2()
    # main_2()
    # main_3()
    # exp_jacobian(np.array([1, 2, 3]), np.array([1.0, 0.5]))
