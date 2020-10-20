# Python Batch Processor

A Python module for performing rate-limited operations in batches, additionally caching outputs.

---

Ideal for hitting APIs, this module accepts an arbitrary function and a list of inputs, and executes the function element-wise per input, caching the outputs to disk and rate limiting the function executions.

The function's consecutive return values are saved to disk, and hence the function is required to return some output value.
