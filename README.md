# k-diffusing

This repository implements SDXL and FLUX text-to-image pipelines which delegate the sampling algorithm to Katherine Crowson's [k_diffusion](https://github.com/crowsonkb/k-diffusion). You may find this repo interesting for the following reasons:
- You want to debug samplers implemented in HuggingFace's `diffusers` against those in `k_diffusion` or other frameworks. This can be very useful if you want to back-port certain samplers in other frameworks back into `diffusers`.
- You prefer a more "functional" style implementation of samplers rather than the more stateful (and IMO much more complicated) design of schedulers in `diffusers`.

Roughly, how this code works is as follows: a closure of the base model (i.e. the UNet) is created inside `__call__` and this is designed to be compatible with what the `k_diffusion` scheduler expects. In the case of SDXL this requires some hacks, namely that the `pipe.scheduler`'s list of sigma scales is copied before it gets mutated into oblivion and that the closure is also able to interpolate an arbitrary sigma value into an integer timestep. For FLUX these hacks are not needed, though a similar style of closure is created and the `to_d` (to derivative) method in `samplers.py` needs to be monkey-patched.

## Samples

To generate samples, run either `python test.py` (for SDXL) or `python test_flux.py` (FLUX). The modified pipelines are under the files `sdxl_comfy_pipeline.py` and `flux_comfy_pipeline.py`.

(Note that FLUX has a different theoretical parameterisation to denoising diffusion so this may explain the bad outputs for some of the schedulers below.)

<table>
<tr>
<th>SDXL</th><th>FLUX-dev</th>
</tr>
<tr>
<td>sdxl - sample_dpm_2<br /><img src="output/sdxl-sample_dpm_2.png" width=400 /></td><td>flux - sample_dpm_2<br /><img src="output/flux-dev-sample_dpm_2.png" width=400 /></td>
</tr>
<tr>
<td>sdxl - sample_dpm_2_ancestral<br /><img src="output/sdxl-sample_dpm_2_ancestral.png" width=400 /></td><td>flux - sample_dpm_2_ancestral<br /><img src="output/flux-dev-sample_dpm_2_ancestral.png" width=400 /></td>
</tr>
<tr>
<td>sdxl - sample_dpmpp_2m<br /><img src="output/sdxl-sample_dpmpp_2m.png" width=400 /></td><td>flux - sample_dpmpp_2m<br /><img src="output/flux-dev-sample_dpmpp_2m.png" width=400 /></td>
</tr>
<tr>
<td>sdxl - sample_dpmpp_2m_sde<br /><img src="output/sdxl-sample_dpmpp_2m_sde.png" width=400 /></td><td>flux - sample_dpmpp_2m_sde<br /><img src="output/flux-dev-sample_dpmpp_2m_sde.png" width=400 /></td>
</tr>
<tr>
<td>sdxl - sample_dpmpp_2s_ancestral<br /><img src="output/sdxl-sample_dpmpp_2s_ancestral.png" width=400 /></td><td>flux - sample_dpmpp_2s_ancestral<br /><img src="output/flux-dev-sample_dpmpp_2s_ancestral.png" width=400 /></td>
</tr>
<tr>
<td>sdxl - sample_dpmpp_3m_sde<br /><img src="output/sdxl-sample_dpmpp_3m_sde.png" width=400 /></td><td>flux - sample_dpmpp_3m_sde<br /><img src="output/flux-dev-sample_dpmpp_3m_sde.png" width=400 /></td>
</tr>
<tr>
<td>sdxl - sample_dpmpp_sde<br /><img src="output/sdxl-sample_dpmpp_sde.png" width=400 /></td><td>flux - sample_dpmpp_sde<br /><img src="output/flux-dev-sample_dpmpp_sde.png" width=400 /></td>
</tr>
<tr>
<td>sdxl - sample_euler<br /><img src="output/sdxl-sample_euler.png" width=400 /></td><td>flux - sample_euler<br /><img src="output/flux-dev-sample_euler.png" width=400 /></td>
</tr>
<tr>
<td>sdxl - sample_euler_ancestral<br /><img src="output/sdxl-sample_euler_ancestral.png" width=400 /></td><td>flux - sample_euler_ancestral<br /><img src="output/flux-dev-sample_euler_ancestral.png" width=400 /></td>
</tr>
<tr>
<td>sdxl - sample_heun<br /><img src="output/sdxl-sample_heun.png" width=400 /></td><td>flux - sample_heun<br /><img src="output/flux-dev-sample_heun.png" width=400 /></td>
</tr>
<tr>
<td>sdxl - sample_lms<br /><img src="output/sdxl-sample_lms.png" width=400 /></td><td>flux - sample_lms<br /><img src="output/flux-dev-sample_lms.png" width=400 /></td>
</tr>

</table>

## Acknowledgements

- [k_diffusion](https://github.com/crowsonkb/k-diffusion)
- The modified pipelines come from `diffusers` with commit hash `aad69ac2f323734a083d66fa89197bf7d88e5a57`
