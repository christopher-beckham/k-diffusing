# repo title

You may find this repo interesting for the following reasons:
- You want to debug samplers implemented in `diffusers` against those in `k-diffusion` or other frameworks. This can be very useful if you want to back-port certain samplers in other frameworks back into diffusers.
- You prefer a more functional-style implementation of samplers rather than the more stateful (and IMO much more complicated) design of schedulers in `diffusers`.

## Files

See:
- `sdxl_comfy_pipeline.py`: SDXL text-to-image pipeline that delegates to k-diffusion samplers.
- `flux_comfy_pipeline.py`: same but for FLUX.

## Samples

To generate samples, run either `python test.py` or `python test_flux.py`. In order for the pipelines to function correctly some hacks must be done.

Note that FLUX has a different theoretical parameterisation to denoising diffusion so this may explain the bad outputs for some of the schedulers below.

<table>
<tr>
    <th>Samples</th>
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